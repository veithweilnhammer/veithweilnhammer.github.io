#!/usr/bin/env python3
"""Generate blog + Substack posts from a single master file (blog.qmd).

You edit ONE file (blog.qmd). This script reads every POST block in it and
writes, for each post whose `status` is `ready` or `published`:

  * an al-folio Jekyll post  ->  ../_posts/<file_date>-<slug>.md
  * a Substack-ready file    ->  substack/<slug>.md

Posts with status `draft` (or missing status) are skipped, so half-written
ideas never leak onto the site.

Usage:
    python3 generate.py            # write all ready/published posts
    python3 generate.py --check    # dry run: list what WOULD be written
    python3 generate.py --source path/to/other.qmd

The master file format is documented at the top of blog.qmd.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: run `python3 -m pip install pyyaml`.")

HERE = os.path.dirname(os.path.abspath(__file__))

CONFIG_RE = re.compile(
    r"<!--\s*BLOG-CONFIG:START\s*-->(.*?)<!--\s*BLOG-CONFIG:END\s*-->",
    re.DOTALL,
)
POST_RE = re.compile(
    r"<!--\s*POST:START\s*-->(.*?)<!--\s*POST:END\s*-->",
    re.DOTALL,
)
# First fenced ```yaml ... ``` block inside a chunk.
YAML_FENCE_RE = re.compile(r"```ya?ml\s*\n(.*?)\n```", re.DOTALL)


def load_yaml_block(text: str, what: str) -> tuple[dict, str]:
    """Return (parsed_yaml, remaining_text_after_the_fence)."""
    m = YAML_FENCE_RE.search(text)
    if not m:
        raise ValueError(f"No ```yaml block found in {what}.")
    data = yaml.safe_load(m.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML block in {what} must be a mapping.")
    return data, text[m.end():]


def read_config(src: str) -> dict:
    m = CONFIG_RE.search(src)
    if not m:
        raise ValueError("No <!-- BLOG-CONFIG:START/END --> block found.")
    cfg, _ = load_yaml_block(m.group(1), "BLOG-CONFIG")
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


def parse_posts(src: str) -> list[tuple[dict, str]]:
    posts = []
    for chunk in POST_RE.findall(src):
        meta, body = load_yaml_block(chunk, "a POST block")
        posts.append((meta, body))
    return posts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", default=os.path.join(HERE, "blog.qmd"))
    ap.add_argument("--posts-dir", default=os.path.join(HERE, "..", "_posts"))
    ap.add_argument("--substack-dir", default=os.path.join(HERE, "substack"))
    ap.add_argument("--check", action="store_true",
                    help="dry run: show what would be written")
    args = ap.parse_args()

    with open(args.source, encoding="utf-8") as fh:
        src = fh.read()

    cfg = read_config(src)
    posts = parse_posts(src)

    generated = 0
    skipped = 0
    seen_slugs: set[str] = set()

    for meta, body in posts:
        slug = str(meta.get("slug", "")).strip()
        status = str(meta.get("status", "draft")).strip().lower()

        if not slug:
            print("! skipping a POST block with no slug")
            continue
        if slug in seen_slugs:
            print(f"! duplicate slug '{slug}' — skipping the second one")
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
