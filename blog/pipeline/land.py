#!/usr/bin/env python3
"""Upsert a POST block into blog.qmd from a finished body file.

Given a slug + metadata + a body file (e.g. a post's final.md, body only, no
front matter), this replaces the existing POST block with that slug, or appends a
new one if none exists. Then run generate.py to emit the Jekyll + Substack files.

Usage:
    python3 land.py --slug the-tell \
        --title "The Tell: ..." --description "..." --date 2026-02-25 \
        --subtitle "..." --tldr "..." --tags movement,mind \
        --sub-tags neuroscience,psychiatry \
        --body posts/the-tell/final.md [--status ready] [--qmd ../blog.qmd]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
POST_RE = re.compile(r"<!--\s*POST:START\s*-->.*?<!--\s*POST:END\s*-->", re.DOTALL)
SLUG_RE = re.compile(r"^\s*slug:\s*(.+?)\s*$", re.MULTILINE)


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(items) + "]"


def build_block(a) -> str:
    tags = [t.strip() for t in a.tags.split(",") if t.strip()] if a.tags else []
    sub_tags = [t.strip() for t in a.sub_tags.split(",") if t.strip()] if a.sub_tags else tags
    with open(a.body, encoding="utf-8") as fh:
        body = fh.read().strip()
    yaml_lines = [
        "```yaml",
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
        "```",
    ]
    return (
        "<!-- POST:START -->\n"
        + "\n".join(yaml_lines)
        + "\n\n"
        + body
        + "\n\n<!-- POST:END -->"
    )


def main() -> None:
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
    p.add_argument("--qmd", default=os.path.join(HERE, "..", "blog.qmd"))
    a = p.parse_args()

    qmd = os.path.abspath(a.qmd)
    with open(qmd, encoding="utf-8") as fh:
        src = fh.read()

    block = build_block(a)

    # Find an existing POST block with this slug.
    replaced = False
    out_parts = []
    last = 0
    for m in POST_RE.finditer(src):
        sm = SLUG_RE.search(m.group(0))
        if sm and sm.group(1).strip() == a.slug:
            out_parts.append(src[last:m.start()])
            out_parts.append(block)
            last = m.end()
            replaced = True
            break
    if replaced:
        out_parts.append(src[last:])
        new_src = "".join(out_parts)
    else:
        # Append a new block at end of file, under a small generated section.
        sep = "" if src.endswith("\n") else "\n"
        new_src = src + f"{sep}\n<!-- landed: {a.slug} -->\n{block}\n"

    with open(qmd, "w", encoding="utf-8") as fh:
        fh.write(new_src)

    action = "replaced" if replaced else "appended"
    print(f"{action} POST block for slug '{a.slug}' in {qmd}")


if __name__ == "__main__":
    main()
