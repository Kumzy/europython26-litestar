# Project Patterns

> Consolidated learnings for this Slidev deck. Read before starting new work to
> prime context. Update at flow completion with elevated patterns.

<!-- truth: start -->
## Conventions

- **Slidev syntax is owned by the vendored skill.** Consult `.agents/skills/slidev/`
  (via the Skill tool) before writing slide frontmatter, layouts, animations, code
  blocks, or export config. Do not guess Slidev features from memory.
- **Slides are one file each under `slides/` (`1.md` … `20.md`).** `slides.md` is
  just the entry: deck headmatter + a `src: ./slides/N.md` import per slide. Edit a
  slide by editing its `slides/N.md`; add/remove/reorder by editing the import list
  in `slides.md`. Per-slide frontmatter (layout/class) goes at the top of `slides/N.md`.
- **Headmatter can carry `src:`** — that's why slide 1 lives in `slides/1.md` while
  deck config stays in `slides.md`. Verified against `@slidev/parser`.
- **Reuse theme classes** from `styles/main.css`: `.kicker` (eyebrow label),
  `.lead` (sub-headline), `.gold` (accent), `.muted` (secondary text), plus the
  card/divider treatments — before authoring new CSS.
- **Diagrams are Vue components**, not images. Prefer `StackCompare`,
  `JourneyCurve`, `MiddlewareChain`, `LayerConfig`, `Star` over static graphics.
- **Code blocks are real Python**, Shiki-highlighted. Keep them idiomatic Litestar
  and accurate; use line-highlighting/transitions purposefully.

## Verification

- There is **no test/lint/typecheck** suite. The verification gate is
  `npm run build` (clean build) plus a visual check in `npm run dev`.
- PDF export (`npm run export-pdf`) needs `playwright-chromium`.

## Gotchas

- Fonts are pinned (`Inter`, `JetBrains Mono`) in headmatter — don't swap ad hoc.
- Two `placeholder`-noted slides still need custom graphics (the "vibe-coder
  stack" image and the website layered-config diagram).
- Speaker split and bios are on slides 1 and 31 — keep attribution accurate.
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
