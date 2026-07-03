# Designing Performant APIs with Litestar — EuroPython 2026

[Slidev](https://sli.dev/) deck for the talk by Cody Fincher & Julien Courtès.
Session: <https://ep2026.europython.eu/session/designing-performant-apis-with-litestar>

## Run

```bash
npm install
npm run dev      # live preview at http://localhost:3030
```

Press `e` in the browser to edit a slide live; arrow keys to navigate.

## Export

```bash
npm run build        # static site -> dist/
npm run export-pdf   # PDF -> dist/slides.pdf  (needs playwright-chromium)
```

## Lint & format

[oxlint] lints the Vue/TS code; [oxfmt] formats the deck (Vue, TS, CSS, JSON,
and the slide Markdown). Both are dev dependencies, so `npm install` is all the
setup they need.

```bash
npm run lint         # lint Vue <script> + TS
npm run lint:fix     # lint and auto-fix
npm run fmt          # format in place
npm run fmt:check    # check formatting (CI-friendly, no writes)
```

Git hooks run these automatically via [prek] (a fast, single-binary drop-in for
`pre-commit`). Install the runner once, then wire up the hook:

```bash
uv tool install prek   # or: brew install prek
prek install           # install the git pre-commit hook
prek run --all-files   # run every hook across the repo
```

Hook config lives in `prek.toml`; tool config in `.oxlintrc.json` / `.oxfmtrc.json`.

[oxlint]: https://oxc.rs/docs/guide/usage/linter
[oxfmt]: https://oxc.rs/docs/guide/usage/formatter
[prek]: https://prek.j178.dev

## Structure

- `slides.md` — deck entry: headmatter (deck config) + `src:` imports of `slides/*.md`.
- `slides/` — one file per slide, `1.md` … `22.md`. Each holds that slide's
  content and its own layout/class frontmatter.
- `styles/main.css` — the Litestar "Stellar Drift" theme (palette, cards, dividers).
- `components/` — Vue components for the diagrams:
  - `StackCompare.vue` — the "what we think we build vs. production reality" hook.
  - `JourneyCurve.vue` — complexity-up / velocity-down chart.
  - `MiddlewareChain.vue` — request → handler pipeline.
  - `LayerConfig.vue` — app / router / controller / handler cascade.
  - `Star.vue` — the five-point star motif.

## Notes

- Code blocks are real, Shiki-highlighted Python — edit them in place.
- Two slides have `placeholder` notes where you may want to drop your own
  graphics (the "vibe-coder stack" image and the website layered-config diagram).
- Speaker split (Cody/Julien) and the bio lines are on slides 1 and 31 — adjust as needed.
