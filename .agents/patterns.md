# Project Patterns

> Consolidated learnings for this Slidev deck. Read before starting new work to
> prime context. Update at flow completion with elevated patterns.

<!-- truth: start -->
## Conventions

- **Slidev syntax is owned by the vendored skill.** Consult `.agents/skills/slidev/`
  (via the Skill tool) before writing slide frontmatter, layouts, animations, code
  blocks, or export config. Do not guess Slidev features from memory.
- **Slides are one file each under `slides/` (`1.md` … `24.md`).** `slides.md` is
  just the entry: deck headmatter + a `src: ./slides/N.md` import per slide. Edit a
  slide by editing its `slides/N.md`; add/remove/reorder by editing the import list
  in `slides.md`. Per-slide frontmatter (layout/class) goes at the top of `slides/N.md`.
- **Headmatter can carry `src:`** — that's why slide 1 lives in `slides/1.md` while
  deck config stays in `slides.md`. Verified against `@slidev/parser`.
- **Standard slide skeleton:** kicker + `#` (h1) title spanning the full slide
  width, one row. Column slides use `layout: two-cols-header` with the title in
  the header and content under `::left::` / `::right::`. Centered statement
  slides and the cover/close are the deliberate exceptions.
- **Reuse theme classes** from `styles/main.css`: `.kicker` (eyebrow label),
  `.lead` (sub-headline), `.gold` (accent), `.muted` (secondary text), plus the
  card/divider treatments — before authoring new CSS.
- **Diagrams are Vue components**, not images. Prefer `StackCompare`,
  `JourneyCurve`, `MiddlewareChain`, `LayerConfig`, `EventLoop`, `Star` over
  static graphics.
- **Code blocks are real Python**, Shiki-highlighted. Keep them idiomatic Litestar
  and accurate; use line-highlighting/transitions purposefully.

## Verification

- The deck's verification gate is `make build` (clean build) plus a visual
  check in `make dev`; `make lint` / `make fix` cover linting and formatting.
- Slide code snippets live in `examples/src/` and are tripwire-tested:
  `uv run pytest`, `uv run ruff check examples`, `uv run pyright`.
- PDF export (`make export-pdf`) needs `playwright-chromium`.

## Gotchas

- Fonts are pinned (`Inter`, `JetBrains Mono`) in headmatter — don't swap ad hoc.
- The former placeholder graphics are now Vue components: the "what we build
  vs. reality" stack (`StackThink`/`StackReality`, slide 2) and the
  layered-config cascade (`LayerConfig`, slide 15). The slide 24 QR
  (`public/qr.svg`) now points at the deck repo; the segno one-liner to
  regenerate it lives in a comment in `slides/24.md`.
- Speaker split and bios are on slides 1 and 24 — keep attribution accurate.
- `.beads/` is git-excluded (local-only); never force-add it.

## Skill Associations

| Domain | Recommended Skill | When to Use |
|--------|-------------------|-------------|
| Slides / Slidev | `slidev` (vendored) | Any slide syntax, layout, animation, code, or export work |
| Vue components | `vue:vue-skilld` | Editing `.vue` diagram components |
| Decision making | `flow:consensus` | Choosing between presentation approaches |
| Challenge claims | `flow:challenge` / `flow:devils-advocate` | Pressure-testing narrative claims |
| Code tracing | `flow:tracer` | Mapping component/style relationships |
| Documentation | `flow:docgen` | Generating supporting docs |
<!-- truth: end -->

---

## Pattern Sources

| Pattern | Source Flow | Date |
|---------|-------------|------|
