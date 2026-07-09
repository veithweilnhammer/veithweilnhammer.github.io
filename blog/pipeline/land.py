#!/usr/bin/env python3
"""Write (or overwrite) a per-post content file from a finished body file.

Given a slug + metadata + a body file (e.g. a post's final.md, body only, no
front matter), this creates `content/<date>-<slug>.md` with YAML front matter
followed by the body. If a content file with the same slug already exists
(under any date-prefixed name), it is overwritten/renamed in place. Then run
generate.py to emit the Jekyll + Substack files.

Usage:
    python3 land.py --slug the-tell \
        --title "The Tell: ..." --description "..." --date 2026-02-25 \
        --subtitle "..." --tldr "..." --tags movement,mind \
        --sub-tags neuroscience,psychiatry \
        --body posts/the-tell/final.md [--status ready] [--content-dir ../content]
"""
from __future__ import annotations

import argparse
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG_RE = re.compile(r"^\s*slug:\s*(.+?)\s*$", re.MULTILINE)


def yaml_list(items):
    return "[" + ", ".join(items) + "]"


def build_doc(a):
    tags = [t.strip() for t in a.tags.split(",") if t.strip()] if a.tags else []
    sub_tags = [t.strip() for t in a.sub_tags.split(",") if t.strip()] if a.sub_tags else tags
    with open(a.body, encoding="utf-8") as fh:
        body = fh.read().strip()
    front = [
        "---",
        f"slug: {a.slug}",
        f'title: "{a.title}"',
        f'description: "{a.description}"',
        f"date: {a.date}",
        f"tags: {yaml_list(tags)}",
        "featured: false",
        f"status: {a.status}",
        "substack:",
        f'  subtitle: "{a.subtitle}"',
        f'  tldr: "{a.tldr}"',
        f"  tags: {yaml_list(sub_tags)}",
        "---",
    ]
    return "\n".join(front) + "\n\n" + body + "\n"


def find_existing(content_dir, slug):
    """Return the path of an existing content file for this slug, if any."""
    for path in glob.glob(os.path.join(content_dir, "*.md")):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as fh:
            m = SLUG_RE.search(fh.read())
        if m and m.group(1).strip() == slug:
            return path
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--description", default="")
    p.add_argument("--date", required=True)
    p.add_argument("--subtitle", default="")
    p.add_argument("--tldr", default="")
    p.add_argument("--tags", default="")
    p.add_argument("--sub-tags", dest="sub_tags", default="")
    p.add_argument("--status", default="ready")
    p.add_argument("--body", required=True)
    p.add_argument("--content-dir", default=os.path.join(HERE, "..", "content"))
    a = p.parse_args()

    content_dir = os.path.abspath(a.content_dir)
    os.makedirs(content_dir, exist_ok=True)

    doc = build_doc(a)
    target = os.path.join(content_dir, f"{a.date}-{a.slug}.md")

    existing = find_existing(content_dir, a.slug)
    if existing and os.path.abspath(existing) != os.path.abspath(target):
        os.remove(existing)
        action = "moved"
    elif existing:
        action = "overwrote"
    else:
        action = "created"

    with open(target, "w", encoding="utf-8") as fh:
        fh.write(doc)

    print(f"{action} content file for slug '{a.slug}' at {target}")


if __name__ == "__main__":
    main()
