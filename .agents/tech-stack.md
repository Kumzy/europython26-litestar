# Tech Stack

<!-- truth: start -->
- **Type:** Slidev presentation (static slide deck) — **not** a runnable app.
- **Presentation framework:** [Slidev](https://sli.dev/) `@slidev/cli ^51` with
  `@slidev/theme-default ^0.25`.
- **UI / components:** Vue 3 (`vue ^3.5`) single-file components for diagrams.
- **Authoring:** Markdown + MDC (`mdc: true`); `slides.md` is the entry that
  imports one file per slide from `slides/` via `src:`. Per-slide frontmatter
  (layout/class) lives at the top of each `slides/N.md`.
- **Code highlighting:** Shiki (`highlighter: shiki`) — real Python snippets.
- **Styling:** custom CSS theme `styles/main.css` ("Stellar Drift"); fonts
  `Inter` + `JetBrains Mono`.
- **Package manager:** **npm** (`package-lock.json` is committed).
- **Subject matter (the talk's topic, not this repo's runtime):** Litestar,
  Advanced Alchemy, SQLSpec, performant Python APIs.
<!-- truth: end -->

## Repository Layout

| Path | Purpose |
|------|---------|
| `slides.md` | Deck entry: headmatter (deck config) + `src:` imports of `slides/*.md`. |
| `slides/` | One file per slide (`1.md` … `22.md`); content + per-slide frontmatter. |
| `styles/main.css` | The "Stellar Drift" theme (palette, cards, dividers, motifs). |
| `styles/index.ts` | Style entry registered by Slidev. |
| `components/` | Vue diagram components (`StackCompare`, `JourneyCurve`, `MiddlewareChain`, `LayerConfig`, `Star`). |
| `package.json` | Scripts: `dev`, `build`, `export`, `export-pdf`. |
| `.agents/` | Flow context + vendored `slidev` skill (tracked). |
| `.beads/` | Beads task DB (local-only, git-excluded). |

## Tooling Notes

- **Authoring skill:** the `slidev` skill is vendored at
  `.agents/skills/slidev/` (registered in `skills-lock.json`). **Consult it for
  all Slidev syntax, layouts, animations, code features, and export work** — it is
  the authoritative reference for this repo. Invoke it via the Skill tool.
- **Export to PDF** requires `playwright-chromium` (see README).
- Node version: whatever satisfies `@slidev/cli ^51` (Node 18+).

## Changing the Stack

Per Flow policy, document any stack change here *before* implementing it
(e.g., swapping themes, adding a Slidev addon, or changing the highlighter).
