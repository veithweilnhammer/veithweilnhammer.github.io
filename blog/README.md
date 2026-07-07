# Blog workspace

Write everything in **one file** — [`blog.qmd`](./blog.qmd) — and generate both
your al-folio blog posts and Substack-ready versions from it.

## Workflow

1. Open `blog.qmd`. Copy the **TEMPLATE** post block into a `# THEME:` section.
2. Write the post. Set its `status:` to `ready` when done.
3. Generate:

   ```bash
   cd blog
   python3 generate.py            # writes the files
   python3 generate.py --check    # dry run — writes nothing
   ```

For each `ready`/`published` post this creates:

- `../_posts/<file_date>-<slug>.md` — al-folio post (same `distill` format as
  your existing posts; front matter, TOC and styling are added automatically).
- `substack/<slug>.md` — paste-ready Substack version with a Title/Subtitle
  block, an auto TL;DR, a visibility checklist, and a canonical link back.

## Notes

- Only `ready`/`published` posts are generated; `draft` posts are ignored.
- `slug` must be unique across the whole file.
- The blog TOC is built from the `## ` headings (Resources/References excluded);
  override it with a `toc:` list in a post's metadata.
- Shared author info and CSS live once in the `BLOG-CONFIG` block in `blog.qmd`.
- This whole `blog/` folder is excluded from the Jekyll build (`_config.yml`),
  so nothing here is published directly.
- Requires PyYAML: `python3 -m pip install pyyaml`.
- Optional: preview the master file with `quarto preview blog.qmd`.
