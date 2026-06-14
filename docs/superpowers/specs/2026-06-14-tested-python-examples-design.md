# Design: Executably-verified Python examples for the Litestar deck

**Date:** 2026-06-14
**Status:** Approved (design) — pending implementation plan
**Author:** Julien Courtès (with Claude)

## Context

This repo is the Slidev deck for the EuroPython 2026 talk _"Designing Performant
APIs with Litestar."_ It is a slide deck, not a runnable app. Five slides embed
Python (`slides/4,5,10,16,17.md`); four of them show **Litestar** code, one
(slide 10) is the **Starlette** "wire-it-yourself" strawman.

Today the snippets are inline string literals. Most are deliberately incomplete
teaching fragments (`...` bodies, undefined symbols). The risk: the talk is ~a
year out, Litestar's API will move, and the speakers are Litestar maintainers —
showing code that no longer imports is the one mistake that can't happen.

## Goal & non-goals

**Goal:** Make the four Litestar snippets _executably verified_ — real `.py`
files that import and run against the currently-installed Litestar — while each
slide stays visually ~identical. The value is **catching API drift before the
talk**, not assertion-heavy unit testing.

**Non-goals:**

- Not testing the Starlette strawman (slide 10) — intentionally "bring your own,"
  not Litestar, no value verifying. Stays inline pseudo-code.
- Not turning terse teaching fragments into full apps on-slide. Supporting code
  lives _outside_ the shown region.
- No CI for now (repo is local-first; Beads is local-only; no `.github` exists).
  prek + `npm run build` are the gates. CI can be added later.

## Mechanism: Slidev region import (verified against installed @slidev/cli)

`<<< @/path/file.py#name lang` imports an external file into a slide.
Confirmed against `node_modules/@slidev/cli/dist/shared-BC4uxnur.js`
(`transformSnippet` / `findRegion`):

- `@/` resolves to the **project root** → `@/examples/src/hello.py` works with
  `examples/` at repo root.
- **Python region markers** (the `#`-comment branch): `# region <name>` …
  `# endregion`. A leading-space variant (`#region`) also matches.
- Region **name** charset is `[\w*-]+` — no spaces, no dots. Use `hello`,
  `requirements`, `controller`, `scopes`.
- Both marker lines are **stripped** from the rendered output and the slice is
  **dedented** — so the `.py` stays valid/runnable while the slide shows only the
  clean inner slice.
- Once a slide uses `<<<`, `npm run build` **throws if the file/region is
  missing** → the deck build becomes a free integration gate.
- Language defaults to the file extension (`py`); we pass `python` explicitly for
  unambiguous Shiki highlighting.

## Layout

```
pyproject.toml            # uv project at REPO ROOT (sources under examples/)
.python-version           # pins a modern CPython (3.13) — uv fetches it
uv.lock                   # committed for reproducible verification
examples/
  README.md
  src/
    hello.py              # slide 4   whole-file import (no region — it IS the snippet)
    orders.py             # slide 5   region: requirements
    controllers.py        # slide 16  region: controller
    di.py                 # slide 17  region: scopes
  tests/
    test_examples.py      # one test module; see per-file table
```

The uv project root is the repo root so `uv` commands run without `cd`; tool
config points at `examples/` (`pythonpath`/`testpaths`/pyright `extraPaths`).

- **Runtime dep:** `litestar`.
- **Dev group:** `pytest`, `httpx` (Litestar `TestClient` needs it), `ruff`,
  `pyright`.
- **pytest config:** `[tool.pytest.ini_options] pythonpath = ["examples/src"]`,
  `testpaths = ["examples/tests"]` so tests `import hello`, `import orders`, etc.
- **pyright:** `extraPaths = ["examples/src"]` (root ≠ the `src` dir, so the
  module search path must be set explicitly).
- **ruff/pyright:** configured for the example code style (idiomatic Litestar:
  PEP 604 unions, async I/O). Consult `litestar` / `litestar-testing` skills when
  authoring so the code is first-party-correct.

## Per-file detail

Each file: imports + supporting symbols **outside** the region; the exact
on-slide snippet **inside** `# region <name>` / `# endregion`.

| Slide | File             | Region         | On-slide body                                                        | Test                                                       |
| ----- | ---------------- | -------------- | -------------------------------------------------------------------- | ---------------------------------------------------------- |
| 4     | `hello.py`       | — (whole file) | real (`return {"msg": "hi"}`) — file _is_ the snippet, imports shown | `TestClient` GET `/hello` → 200 + body                     |
| 5     | `orders.py`      | `requirements` | keep `...` (the point is "look how much arrives")                    | app builds; `/orders` registered; OpenAPI schema generates |
| 16    | `controllers.py` | `controller`   | **real one-liner** `return await svc.list()`                         | `TestClient` GET `/orders` → 200 + JSON list               |
| 17    | `di.py`          | `scopes`       | `Provide(...)` lines + comments, as today                            | app builds; dependency resolves (scope wiring compiles)    |

**Slide 5 supporting symbols** (defined outside region, real stubs): `User`,
`Session`, `OrderDTO`, `require_user` guard. **Slide 16**: a tiny real
`OrderService` (so the response assertion is meaningful), `OrderDTO`, `order_svc`
provider. **Slide 17**: real `get_session` / `get_client` providers wired into a
`Litestar(dependencies=...)` below the region.

### One flagged on-slide content change

Slide 16's `...` body becomes `return await svc.list()` (user-approved). Slides
4, 5, 17 keep their current on-slide appearance.

### Slide directive examples

```md
<<< @/examples/src/hello.py python
<<< @/examples/src/orders.py#requirements python
<<< @/examples/src/controllers.py#controller python
<<< @/examples/src/di.py#scopes python
```

Each replaces the corresponding inline ` ```python … ``` ` block. The
`placeholder` notes on slides 4 and 5 are removed (the code is now real).

## Verification wiring

- **prek** (`prek.toml`): new `local` hook, `language = system`,
  `files = ^examples/.*\.(py|toml)$`, `pass_filenames = false`, entry:
  `cd examples && uv run ruff check . && uv run ruff format --check . && uv run pyright && uv run pytest -q`.
- **`npm run build`**: unchanged command, now also verifies every `<<<` file +
  region resolves. Canonical "does it still build?" gate.
- **`.gitignore`**: add `examples/.venv/`, `__pycache__/`, `.pytest_cache/`,
  `.ruff_cache/`. (`*.db` already ignored; examples use in-memory only.)

## Gotchas / decisions captured

- Region names: `[\w*-]+` only — no dots/spaces.
- `# region` markers are plain Python comments → harmless to runtime, stripped on
  slide.
- Keep `examples/` deps minimal; TestClient pulls `httpx` (dev-only).
- System Python is 3.9.6; uv manages a modern interpreter (3.13) independently.
- Slide 10 (Starlette) is **out of scope** — stays inline.

## Implementation task outline

1. `uv init` the `examples/` sub-project; pin Python; add deps + dev group.
2. Author the four `src/*.py` files with regions (consult Litestar skills).
3. Author `tests/test_examples.py` per the table.
4. `uv run ruff/pyright/pytest` green.
5. Rewrite slides 4, 5, 16, 17 to `<<<` imports; drop placeholder notes.
6. `npm run build` green (verifies imports + regions render).
7. Add the prek hook; update `.gitignore`.
8. Final: `prek run --all-files` + `npm run build` both clean.

## Implementation outcome (2026-06-14)

Done and verified. Litestar resolved to **2.24.0** (pinned in `examples/uv.lock`).

Gates, all green:

- `ruff check` + `ruff format --check`: clean (6 files)
- `pyright`: 0 errors
- `pytest`: 4 passed
- `npm run build`: `✓ built` — all four `<<<` region imports resolve and render
- Each rendered region slice was extracted with Slidev's own `findRegion`/dedent
  logic and visually confirmed (no trailing blanks; comments preserved).

### Deprecation finding (the payoff)

On the very first `pytest` run, Litestar 2.24 emitted 6 `LitestarDeprecationWarning`s:
the **inferred** DI style (`svc: OrderService`, `user`, `db`, `session`, `client`)
and inferred query param (`page: int = 1`) on slides 5/16/17 are deprecated and
**stop working in Litestar 3.0** (3.0 wants `NamedDependency[...]` / `FromQuery[int]`).

**Decision (user):** keep the clean **2.x inferred** idiom on the slides — it's
how the majority of current Litestar code reads and is clearest on a slide. The
warnings are **informational**, not gate failures (pytest shows them; no
`filterwarnings = error`). Revisit the idiom near the talk if Litestar 3.0 ships.

### Cosmetic deltas vs. the original inline snippets

- Slides 4 & 16: 2 blank lines between top-level defs (PEP8) instead of 1.
- Slide 5: inline-comment padding normalized to a single space by `ruff format`.
- Slide 16: `...` body replaced by the real one-liner `return await svc.list()`
  (user-approved) so the test asserts a real JSON response.

### Files

- New (repo root): `pyproject.toml`, `.python-version`, `uv.lock`.
- New: `examples/README.md`, `examples/src/{hello,orders,controllers,di}.py`,
  `examples/tests/{conftest.py,test_examples.py}`.
- Edited: `slides/{4,5,16,17}.md` (→ `<<<` imports; placeholder notes removed on
  4 & 5), `prek.toml` (+`examples` hook), `.gitignore` (+Python ignores).
