# Blog production pipeline

A multi-agent pipeline for producing one blog post. Everything here lives under
`blog/`, which is excluded from the Jekyll build, so nothing is published until
the final body is landed as a `content/<date>-<slug>.md` file and `generate.py`
is run.

## Roles

The core idea: **integrate both the search and the writing across models.** The
pipeline alternates between parallel divergence (three frontier models work
independently) and editorial convergence (one editor synthesizes their work),
twice — once for drafting, once for review.

| Stage | Who | Model (default) | Output |
|-------|-----|-----------------|--------|
| 0. Brief | orchestrator | Opus 4.8 (the CLI) | `posts/<slug>/brief.md` |
| 1. Research + Draft ×3 | 3 parallel agents | Gemini 3.1 Pro · GPT-5.5 · Opus 4.8 | `posts/<slug>/candidates/{gemini,gpt,opus}.md` |
| 2. Integrate draft | editor | Opus 4.8 (the CLI) | `posts/<slug>/integrated.md` |
| 3. Review ×3 | 3 parallel agents | Gemini 3.1 Pro · GPT-5.5 · Opus 4.8 | `posts/<slug>/reviews/{gemini,gpt,opus}.md` |
| 4. Integrate reviews + rewrite | editor | Opus 4.8 (the CLI) | `posts/<slug>/final.md` |
| 5. Land | orchestrator | Opus 4.8 (the CLI) | `../content/<date>-<slug>.md` via `land.py` + `generate.py` |

Stage 1: each of the three models independently does deep web research **and**
writes a complete candidate post. Each candidate file has an **evidence** section
(verified sources, exact public-domain quotes, flagged uncertainties) and a
**full draft** written to `writing_style.md`.

Stage 2: the editor fact-checks against the union of the three evidence sections
and synthesizes one integrated draft — best framing, structure, and sentences
across the three candidates, weakest/unverifiable material dropped.

Stage 3: the same three models each independently review the integrated draft
against `writing_style.md` (banned constructions, jargon, grounding, structure),
producing specific, quote-level notes.

Stage 4: the editor merges the three review sets (keeping points ≥2 reviewers
raise, or any single high-confidence factual/style catch) and produces the final
rewrite.

The orchestrator/editor is the Copilot CLI session itself. It launches every
parallel stage as sub-agents with the `task` tool, using the `model` parameter to
pick the model per agent, and does the two integration stages inline.

## Authoritative inputs (every agent is given these)

- `../writing_style.md` — the voice. This is the single most important input for
  stages 1, 3, 4.
- `../blog_ideas.md` — the full list of planned posts, used only so posts don't
  repeat the same material; posts are standalone and never cross-link.
- `posts/<slug>/brief.md` — this post's spec: topic, angle, anchors, what it must
  cover, what it must not re-tell (material other posts develop), target length.

## How to run a post (reproducible)

1. **Create the workspace:**
   `mkdir -p pipeline/posts/<slug>/{candidates,reviews}`
2. **Write the brief:** copy `posts/_TEMPLATE_brief.md` to
   `posts/<slug>/brief.md` and fill it in (or ask the orchestrator to draft it
   from the series bible + the idea backlog in `../blog_ideas.md`).
3. **Set models:** copy `posts/_TEMPLATE_config.yml` to `posts/<slug>/config.yml`
   and choose the models for each stage (the three parallel slots + which model
   edits).
4. **Ask the orchestrator to "run the pipeline for <slug>."** It will:
   - launch the 3 research+draft agents in parallel (prompt =
     `prompts/research_and_draft.md`) → `candidates/`,
   - integrate them into `integrated.md`,
   - launch the 3 review agents in parallel (prompt = `prompts/review.md`) →
     `reviews/`,
   - integrate the reviews and rewrite into `final.md`,
   - land `final.md` as a `../content/<date>-<slug>.md` file (via `land.py`) and
     run `generate.py`.
5. **Review `final.md` yourself**, then approve landing.

Each stage writes files, so a run can be resumed or re-run stage-by-stage
without repeating earlier stages.

## Prompt templates

Prompts in `prompts/` are parametrized with `{{slug}}`, `{{post_dir}}`,
`{{model_label}}`, etc. The orchestrator fills these in when launching each
agent. Edit the templates once to change behavior for all future posts.

- `research_and_draft.md` — stage 1 (run by each of the 3 models).
- `review.md` — stage 3 (run by each of the 3 models).

Integration (stages 2 and 4) is done by the editor inline, guided by this README.

## Conventions

- Stage-1 agents must only report **real, verifiable** sources (prefer DOI /
  stable URL) and must flag anything they could not verify. No invented
  citations. Public-domain quotes must be verified against the source.
- The editor's integrated draft is grounded **only** in the union of the three
  candidates' verified evidence — no new unverified facts introduced at
  integration time.
- Keep citations light (it's a blog); overflow goes into a "Further reading"
  list. See `../writing_style.md`.
- Every stage-1 and stage-3 agent receives `../writing_style.md` verbatim and is
  judged against it.

