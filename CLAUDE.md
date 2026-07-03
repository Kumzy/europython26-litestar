# CLAUDE.md

Project context for Claude Code. This repo is the **Slidev presentation** for the
EuroPython 2026 talk _"Designing Performant APIs with Litestar"_ by Cody Fincher &
Julien Courtès. It is a slide deck — **not** a runnable Litestar application.

## Source of Truth

Flow context lives in `.agents/`. Read these first:

- **[.agents/product.md](.agents/product.md)** — what the deck is and its goals.
- **[.agents/tech-stack.md](.agents/tech-stack.md)** — Slidev + Vue stack and repo layout.
- **[.agents/product-guidelines.md](.agents/product-guidelines.md)** — tone + "Stellar Drift" brand.
- **[.agents/workflow.md](.agents/workflow.md)** — commands, principles, Beads workflow.
- **[.agents/patterns.md](.agents/patterns.md)** — conventions to reuse.
- **[.agents/index.md](.agents/index.md)** — full file-resolution map.

## Use the Slidev Skill

The authoritative reference for all slide work is the vendored **`slidev`** skill
at `.agents/skills/slidev/` (registered in `skills-lock.json`). **Invoke it via the
Skill tool before writing or changing slides, layouts, animations, code blocks, or
export config** — do not guess Slidev syntax from memory.

## Commands

All workflows go through the `Makefile` (`make help` lists every target):

```bash
make install     # install deps (npm + uv) and prek git hooks
make dev         # live preview at http://localhost:3030
make build       # static site -> dist/  (the "does it still build?" check)
make export-pdf  # PDF -> dist/slides.pdf  (needs playwright-chromium)
make lint        # oxlint + ruff + pyright
make fix         # oxfmt + ruff format
make test        # example tripwire tests (pytest)
make prek        # run every git hook across the repo
```

**prek** (a fast `pre-commit` drop-in) runs the linters/formatters as git hooks —
see `prek.toml`, `.oxlintrc.json`, `.oxfmtrc.json`, and the README. A clean
`make build` is still the canonical verification gate. Slides are one file
each in `slides/` (`1.md` … `23.md`), imported by `slides.md` via `src:`; theme
in `styles/main.css`; diagrams in `components/*.vue`. The formatter intentionally
ignores `slides.md` (the Slidev `src:` manifest) and `.agents/`.

## Flow & Beads

- Tasks are tracked in Beads (`bd`, prefix `ep26`), configured **local-only**.
- `.agents/` is git-tracked (shared); `.beads/` is git-excluded (local-only) —
  never force-add it.
- Use `/flow:*` slash commands for the Flow lifecycle; run `/flow:sync` after
  Beads state changes when policy requires.
