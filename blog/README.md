# Blog

Source for the al-folio (Jekyll) blog and its Substack cross-posts. Everything
under `blog/` is **excluded from the Jekyll build** — nothing here is published
directly. You write one file per post, run one generator, and it emits the real
site files.

---

## TL;DR — the everyday workflow

```bash
cd blog

# 1. write / proofread a post: edit its file in content/
#    (front matter + body, one post per file)
$EDITOR content/2026-02-25-the-tell.md

# 2. regenerate the site + Substack files
python3 generate.py            # writes the real files
python3 generate.py --check    # dry run: shows what would be written, writes nothing
```

That's it. To publish a post, set `status: ready` in its front matter and run
`generate.py`. To take one down, set `status: draft` and regenerate (then delete
the stale output file if you want it gone from the site).

---

## Folder map

```
blog/
├── content/                 # ← SOURCE OF TRUTH. One file per post.
│   ├── 2026-02-25-the-tell.md
│   ├── 2026-03-04-regulate-ai-therapy-by-use.md
│   ├── … (one <date>-<slug>.md per post)
│   └── _template.md         # copy-me starter (leading "_" = ignored by the generator)
├── config.yml               # shared author info + CSS, applied to every post
├── generate.py              # content/*.md + config.yml  →  the two outputs below
│
├── ../_posts/<date>-<slug>.md   # OUTPUT: al-folio Jekyll posts (what the site renders)
├── substack/<slug>.md           # OUTPUT: paste-ready Substack versions
│
├── writing_style.md         # the voice + hard ban list (used by you and the pipeline)
├── blog_ideas.md            # backlog of post ideas
├── style_inbox.md           # scratch pad for style tweaks to fold into writing_style.md
└── pipeline/                # the multi-agent drafting pipeline (see pipeline/README.md)
```

**Never edit the outputs** (`../_posts/*` or `substack/*`) — `generate.py`
overwrites them. Edit `content/*` and regenerate.

---

## A post file

Each post is a normal Markdown file with YAML front matter, then the body:

```markdown
---
slug: the-tell                         # unique; becomes the output filename + URL
title: "The Tell: ..."
description: "One-line summary (blog meta + Substack fallback subtitle)."
date: 2026-02-25                        # date shown on the post
# file_date: 2026-02-25                 # optional: date used only in the OUTPUT filename
tags: [mental health, psychiatry]
featured: false
status: ready                          # draft | ready | published (only ready/published generate)
# toc: [Section A, Section B]           # optional: force a sidebar TOC
substack:
  subtitle: "Hook / SEO subtitle shown in previews and email."
  tldr: "One-sentence takeaway shown at the very top on Substack."
  tags: [neuroscience, mental health]
---

Body starts here — plain prose, with or without `## ` headings.
```

Field notes:

- **`slug`** must be unique across `content/`. It sets the output filename and
  the blog URL. Renaming the file does not change the slug (the front matter
  wins), but the convention is `content/<date>-<slug>.md`.
- **`status`** — only `ready` or `published` are generated. `draft` (or missing)
  is skipped, so half-written posts never leak onto the site. Files named with a
  leading `_` (e.g. `_template.md`) are ignored regardless of status.
- **Headings → sidebar TOC.** If the body uses `## ` headings they become the
  post's sidebar table of contents automatically; a `## Resources`,
  `## References`, `## Further reading`, or `## Notes` heading is left out. Set a
  `toc:` list in the front matter to override, or use no `## ` headings for no
  sidebar.
- **`substack:`** drives the `substack/<slug>.md` header (subtitle/SEO hook,
  TL;DR line, discovery tags). The generator also auto-appends a canonical link
  back to the blog post and a subscribe/share line.
- **`file_date`** is only needed if you want the output filename dated
  differently from the displayed `date`; it defaults to `date`.

Shared author info and the injected CSS live once in **`config.yml`** — edit
there to change them for every post at once.

---

## Adding a new post by hand

```bash
cd blog
cp content/_template.md content/2026-08-01-my-new-post.md
$EDITOR content/2026-08-01-my-new-post.md     # fill in front matter + write the body
# set status: ready when it's done
python3 generate.py
```

## Adding a post with the drafting pipeline

For research-heavy posts, the multi-agent pipeline in `pipeline/` drafts,
reviews, and finalizes a post, then lands it as a `content/` file:

```bash
cd blog
python3 pipeline/land.py --slug my-new-post \
  --title "My New Post" --description "..." --date 2026-08-01 \
  --subtitle "..." --tldr "..." --tags tag-a,tag-b --sub-tags neuroscience \
  --body pipeline/posts/my-new-post/final.md --status ready
python3 generate.py
```

`land.py` writes (or overwrites) `content/<date>-<slug>.md` from a body-only
file. See **`pipeline/README.md`** for the full drafting workflow.

---

## Proofreading

Open the post's file in `content/` and edit prose (and metadata) in place — it is
the single source of truth, so there is no sync step and no risk of edits being
overwritten. When done, run `python3 generate.py` to refresh the site and
Substack copies. Do a final skim of `writing_style.md` for the hard ban list.
