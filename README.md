# Designing Performant APIs with Litestar — EuroPython 2026

[Slidev](https://sli.dev/) deck for the talk by Cody Fincher & Julien Courtès.

Session: <https://ep2026.europython.eu/session/designing-performant-apis-with-litestar>

Litestar: <https://litestar.dev>

Discord: <https://discord.gg/litestar>

## Run

```bash
make install     # install deps (npm + uv) and git hooks
make dev         # live preview at http://localhost:3030
```

Run `make help` to list all available commands.
Press `e` in the browser to edit a slide live; arrow keys to navigate.

## Export

```bash
make build       # static site -> dist/
make export-pdf  # PDF -> dist/slides.pdf  (needs playwright-chromium)
```

## Lint, format & test

[oxlint] lints the Vue/TS code; [oxfmt] formats the deck (Vue, TS, CSS, JSON,
and the slide Markdown). [ruff] and [pyright] cover the Python examples.

```bash
make lint        # oxlint + ruff + pyright
make fix         # format in place (oxfmt + ruff format)
make test        # example tripwire tests (pytest)
make prek        # run every git hook across the repo
```

Git hooks run automatically via [prek] (a fast, single-binary drop-in for
`pre-commit`); `make install` wires them up. Hook config lives in `prek.toml`;
tool config in `.oxlintrc.json` / `.oxfmtrc.json`.

[oxlint]: https://oxc.rs/docs/guide/usage/linter
[oxfmt]: https://oxc.rs/docs/guide/usage/formatter
[ruff]: https://docs.astral.sh/ruff/
[pyright]: https://microsoft.github.io/pyright/
[prek]: https://prek.j178.dev

## Structure

- `slides.md` — deck entry: headmatter (deck config) + `src:` imports of `slides/*.md`.
- `slides/` — one file per slide (`1.md` … `23.md`), content + per-slide frontmatter.
- `styles/` — the Litestar "Stellar Drift" theme.
- `components/` — Vue components for the diagrams.
- `examples/` — runnable Litestar snippets rendered into the slides.
- `public/` — static assets (logo, memes, QR).
