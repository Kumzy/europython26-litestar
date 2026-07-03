# Project Workflow

This is a **Slidev presentation** repo, not a software application. There is no
test suite, type checker, or deployment target — the deliverable is a slide deck.
The workflow below is adapted accordingly; "verification" here means *the deck
builds and looks right*, not "tests pass."

<!-- truth: start -->
## Essential Commands

All workflows go through the `Makefile`; run `make help` to list every target.

### Daily Development
```bash
make install         # install deps (npm + uv) and prek git hooks (first run)
make dev             # live preview at http://localhost:3030 (press `e` to edit a slide)
```

### Build & Export (the "verify" step)
```bash
make build           # static site -> dist/  (the canonical "does it still build?" check)
make export-pdf      # PDF -> dist/slides.pdf  (needs playwright-chromium)
```

### Lint, Format & Test
```bash
make lint            # oxlint + ruff + pyright
make fix             # oxfmt + ruff format
make test            # example tripwire tests (pytest)
make prek            # run every git hook across the repo
```

Treat a clean `make build` as the verification gate before committing content
changes.

## Guiding Principles

1. **Use the Slidev skill.** The vendored `slidev` skill at `.agents/skills/slidev/`
   is the authoritative reference for all slide syntax, layouts, animations, code
   blocks, components, and export behavior. Consult it (via the Skill tool) before
   writing or changing slides — don't guess Slidev syntax.
2. **Beads is the Source of Truth** for tasks. Run `/flow:sync` to export task
   state to `spec.md` when `syncPolicy.flowSyncAfterMutation` is enabled.
3. **Content lives in `slides/N.md`** (one file per slide), imported by `slides.md`
   via `src:`. Keep the narrative coherent slide-to-slide; prefer the custom Vue
   diagrams in `components/` over static images.
4. **Stay on-brand.** Reuse the "Stellar Drift" theme classes in `styles/main.css`
   (`.kicker`, `.lead`, `.gold`, `.muted`, cards, dividers) before adding new CSS.
5. **Code on slides must be real and correct.** Snippets are Shiki-highlighted
   Python — keep them idiomatic Litestar and accurate.
6. **Verify visually.** After meaningful changes, run `make build` (and the
   live preview) to confirm the deck still renders and exports.
7. **Minimal targeted changes.** Make the smallest coherent edit that achieves the
   goal; don't opportunistically restyle unrelated slides.
8. **No silent descoping.** If a change is bigger than expected, refine the plan
   or ask — don't quietly skip slides or content.
<!-- truth: end -->

## Beads Integration

Flow uses official Beads (`bd`) configured for **local-only** use during setup.

- Backend: `bd` (Dolt, embedded). Issue prefix: `ep26`.
- `.beads/` is git-excluded via `.git/info/exclude` (local-only).
- `beads.json` sets `syncPolicy.autoExport: false`, `autoGitAdd: false`,
  `allowDoltPush: false`; `bd config` sets `no-git-ops`, `export.auto`,
  `export.git-add` to off; `.beads/config.yaml` opts into `json-envelope: true`.

### Session Protocol

- **Start:** `bd prime --mcp` when host hooks inject MCP context; otherwise `bd prime`.
- **End:** prefer `.git/info/exclude` for local-only ignores. Do **not** run
  `bd dolt push` unless explicitly requested.

### When to Track in Beads

**Rule: if work takes >5 minutes, track it in Beads.** For a deck, that means a
new section, a reworked narrative arc, a new diagram component, or a theme change
— not a one-word typo fix.

```bash
bd create "<task>" -t task -p 2 --description="<purpose and goal>"
bd note <id> "<context for future agents>"
```

Priority levels: P0=critical, P1=high, P2=medium, P3=low, P4=backlog.

## Task Workflow (adapted for a deck)

Beads is the source of truth — never hand-edit `[x]`/`[~]`/`[!]`/`[-]` markers in
`spec.md`; run `/flow:sync` after Beads state changes.

1. **Select task** from the Beads ready queue.
2. **Mark in progress** in Beads (don't edit `spec.md` directly).
3. **Make the change** — edit the relevant `slides/N.md` (or `slides.md` to
   add/reorder slides), `styles/`, or `components/`.
4. **Verify visually:** run `make dev` to eyeball it and `make build` to
   confirm it still compiles/exports. (This replaces the TDD red/green cycle —
   there are no unit tests for slides.)
5. **Document stack deviations** in `tech-stack.md` *before* implementing them
   (new addon, theme swap, highlighter change).
6. **Commit** with a clear conventional-commit message (see below).
7. **Close in Beads** with the commit hash; run `/flow:sync` if policy requires.
8. **Log learnings** — elevate reusable conventions to `.agents/patterns.md` and
   synthesize durable knowledge into `.agents/knowledge/` chapters.

### Companion Skills

- **`slidev`** (vendored) — Slidev syntax, layouts, animations, export. **Primary.**
- `flow:tracer` — explore how components/styles connect before a big edit.
- `flow:consensus` — choose between presentation approaches.
- `flow:challenge` / `flow:devils-advocate` — pressure-test narrative claims.
- `flow:docgen` — generate supporting docs if needed.

### Knowledge Flywheel

1. **Capture** learnings after each task.
2. **Elevate** reusable patterns (theme classes, component conventions, Slidev
   gotchas) to `.agents/patterns.md`.
3. **Synthesize** durable knowledge into `.agents/knowledge/*.md` chapters.
4. **Inherit** — new work reads `patterns.md` + scans `.agents/knowledge/`.

## Commit Guidelines

Conventional commits. Suggested scopes for this repo: `slides`, `theme`,
`components`, `build`, `docs`, `chore`.

```bash
git commit -m "feat(slides): Add section on middleware ordering"
git commit -m "style(theme): Tune gold accent contrast for projector"
git commit -m "fix(components): Correct MiddlewareChain arrow alignment"
git commit -m "docs(readme): Update export instructions"
```

## Definition of Done

A content task is complete when:

1. The change is implemented in `slides.md` / `styles/` / `components/`.
2. `make build` succeeds (and the slide looks right in `make dev`).
3. Narrative still flows and the deck stays on-brand.
4. Changes committed with a proper conventional-commit message.
5. Task closed in Beads with the commit reference; `/flow:sync` run if policy requires.
6. No git-excluded Flow artifacts (`.beads/`) were force-added.
