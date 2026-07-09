#!/usr/bin/env python3
"""Generate blog + Substack posts from per-post source files.

Each post lives in its own file under `content/` with YAML front matter
followed by the body:

    ---
    slug: my-post
    title: "..."
    date: 2026-01-01
    status: ready
    ...
    ---

    Body text here.

For every post whose `status` is `ready` or `published`, this writes:

  * an al-folio Jekyll post  ->  ../_posts/<file_date>-<slug>.md
  * a Substack-ready file    ->  substack/<slug>.md

Posts with status `draft` (or missing status) are skipped, and files whose
name starts with `_` (e.g. `_template.md`) are ignored entirely.

Shared author + styling live in `config.yml`.

Usage:
    python3 generate.py            # write all ready/published posts
    python3 generate.py --check    # dry run: list what WOULD be written
    python3 generate.py --content-dir path/to/content --config path/to/config.yml
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: run `python3 -m pip install pyyaml`.")

HERE = os.path.dirname(os.path.abspath(__file__))

# Front matter delimited by a leading `---` line and the next `---` line.
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.DOTALL)


def split_front_matter(text: str, what: str) -> tuple[dict, str]:
    """Return (parsed_front_matter, body). Body may contain `---` lines."""
    m = FRONT_MATTER_RE.match(text)
    if not m:
        raise ValueError(f"No `---` front matter found in {what}.")
    data = yaml.safe_load(m.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Front matter in {what} must be a mapping.")
    return data, m.group(2)


def read_config(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh.read()) or {}
    if not isinstance(cfg, dict):
        raise ValueError(f"{path} must contain a YAML mapping.")
    return cfg


def h2_headings(body: str) -> list[str]:
    return [
        line[3:].strip()
        for line in body.splitlines()
        if line.startswith("## ") and not line.startswith("### ")
    ]


def build_toc(meta: dict, body: str) -> list[str]:
    if meta.get("toc"):
        return list(meta["toc"])
    # Auto: every H2 except back-matter (Resources / References / Notes ...).
    skip_prefixes = ("resources", "references", "further reading", "notes")
    return [
        h for h in h2_headings(body)
        if not h.strip().lower().startswith(skip_prefixes)
    ]


def yaml_inline_list(items) -> str:
    items = items or []
    return "[" + ", ".join(str(i) for i in items) + "]"


def indent(text: str, spaces: int) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line else line for line in text.splitlines())


def render_jekyll(meta: dict, body: str, cfg: dict) -> str:
    author = cfg.get("author", {})
    styles = cfg.get("styles", "").rstrip("\n")
    toc = build_toc(meta, body)

    fm = []
    fm.append("---")
    fm.append("layout: distill")
    fm.append(f'title: "{meta["title"]}"')
    fm.append(f'description: "{meta.get("description", "")}"')
    fm.append(f'tags: {yaml_inline_list(meta.get("tags"))}')
    fm.append("categories:")
    fm.append("giscus_comments: false")
    fm.append(f"date: {meta['date']}")
    fm.append(f"featured: {str(bool(meta.get('featured', False))).lower()}")
    fm.append("")
    fm.append("authors:")
    fm.append(f"  - name: {author.get('name', '')}")
    fm.append(f"    url: \"{author.get('url', '')}\"")
    fm.append("    affiliations:")
    fm.append(f"      name: {author.get('affiliation', '')}")
    fm.append("")
    if toc:
        fm.append("toc:")
        for name in toc:
            fm.append(f"  - name: {name}")
        fm.append("")
    fm.append("_styles: >")
    fm.append(indent(styles, 2))
    fm.append("---")
    return "\n".join(fm) + "\n\n" + body.strip() + "\n"


def render_substack(meta: dict, body: str, cfg: dict) -> str:
    sub = meta.get("substack", {}) or {}
    slug = meta["slug"]
    site = cfg.get("author", {}).get("url", "").rstrip("/")
    blog_url = f"{site}/blog/{slug}/" if site else ""
    tags = sub.get("tags") or meta.get("tags") or []

    header = [
        "<!--",
        "==========================================================",
        "SUBSTACK — copy these into the editor's Title / Subtitle boxes:",
        f"  Title:    {meta['title']}",
        f"  Subtitle: {sub.get('subtitle', meta.get('description', ''))}",
        "----------------------------------------------------------",
        f"  Suggested tags: {', '.join(str(t) for t in tags)}",
        "  Visibility checklist:",
        "    [ ] Subtitle doubles as an SEO hook (done above)",
        "    [ ] TL;DR in the first 2 lines",
        "    [ ] 1-2 internal links to related posts",
        "    [ ] Scannable subheads",
        "    [ ] Clear subscribe / share CTA at the end",
        f"    [ ] Canonical / cross-post link back to {blog_url or 'your blog'}",
        "==========================================================",
        "Paste everything BELOW this comment into the Substack body.",
        "-->",
    ]
    parts = ["\n".join(header), ""]
    if sub.get("tldr"):
        parts.append(f"**TL;DR — {sub['tldr']}**")
        parts.append("")
    parts.append(body.strip())
    parts.append("")
    parts.append("---")
    if blog_url:
        parts.append(
            f"*Originally posted on [my blog]({blog_url}). "
            "If this was useful, consider subscribing and sharing.*"
        )
    else:
        parts.append("*If this was useful, consider subscribing and sharing.*")
    return "\n".join(parts) + "\n"


def parse_posts(content_dir: str) -> list[tuple[dict, str, str]]:
    """Read every content/*.md (skipping names starting with `_`).

    Returns a list of (meta, body, source_path), sorted by filename.
    """
    posts = []
    pattern = os.path.join(content_dir, "*.md")
    for path in sorted(glob.glob(pattern)):
        name = os.path.basename(path)
        if name.startswith("_"):
            continue
        with open(path, encoding="utf-8") as fh:
            meta, body = split_front_matter(fh.read(), name)
        posts.append((meta, body, path))
    return posts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content-dir", default=os.path.join(HERE, "content"))
    ap.add_argument("--config", default=os.path.join(HERE, "config.yml"))
    ap.add_argument("--posts-dir", default=os.path.join(HERE, "..", "_posts"))
    ap.add_argument("--substack-dir", default=os.path.join(HERE, "substack"))
    ap.add_argument("--check", action="store_true",
                    help="dry run: show what would be written")
    args = ap.parse_args()

    cfg = read_config(args.config)
    posts = parse_posts(args.content_dir)

    generated = 0
    skipped = 0
    seen_slugs: set[str] = set()

    for meta, body, path in posts:
        name = os.path.basename(path)
        slug = str(meta.get("slug", "")).strip()
        status = str(meta.get("status", "draft")).strip().lower()

        if not slug:
            print(f"! skipping {name}: no slug")
            continue
        if slug in seen_slugs:
            print(f"! duplicate slug '{slug}' in {name} — skipping")
            continue
        seen_slugs.add(slug)

        if status not in ("ready", "published"):
            skipped += 1
            continue
        for field in ("title", "date"):
            if not meta.get(field):
                print(f"! '{slug}' is {status} but missing '{field}' — skipping")
                skipped += 1
                break
        else:
            file_date = str(meta.get("file_date") or meta["date"])
            jekyll_path = os.path.normpath(
                os.path.join(args.posts_dir, f"{file_date}-{slug}.md"))
            substack_path = os.path.normpath(
                os.path.join(args.substack_dir, f"{slug}.md"))

            jekyll = render_jekyll(meta, body, cfg)
            substack = render_substack(meta, body, cfg)

            if args.check:
                print(f"[check] would write {jekyll_path}")
                print(f"[check] would write {substack_path}")
            else:
                with open(jekyll_path, "w", encoding="utf-8") as fh:
                    fh.write(jekyll)
                with open(substack_path, "w", encoding="utf-8") as fh:
                    fh.write(substack)
                print(f"wrote {jekyll_path}")
                print(f"wrote {substack_path}")
            generated += 1

    print(f"\n{generated} post(s) {'to generate' if args.check else 'generated'}, "
          f"{skipped} draft/incomplete skipped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
