# Deck examples

Real, runnable Litestar snippets that are **rendered directly into the slides**
via Slidev's code-import (`<<< @/examples/src/<file>.py#<region> python`).

The point isn't unit-test coverage — it's a tripwire: these import and run
against the **currently-pinned Litestar**, so if the API drifts before the talk,
`pytest` / `npm run build` fail instead of a projector.

The uv project lives at the **repo root** (`pyproject.toml`); these are its
sources. Run everything from the repo root:

```bash
uv sync                       # create .venv + install (run once)
uv run ruff check examples    # lint
uv run ruff format examples   # format
uv run pyright                # types (configured to examples/)
uv run pytest                 # verify each example app builds / responds
```

Each `src/*.py` file is a complete program; `# region <name>` / `# endregion`
markers select the exact slice shown on a slide (markers are stripped + dedented
by Slidev). Supporting code lives outside the region.

| File                 | Slide | Region               |
| -------------------- | ----- | -------------------- |
| `src/hello.py`       | 3     | whole file           |
| `src/orders.py`      | 4     | `requirements`       |
| `src/controllers.py` | 12    | `controller`         |
| `src/di.py`          | 13    | `scopes`             |
| `src/blocking.py`    | 18    | `blocking` + `fixed` |
| `src/dtos.py`        | 19    | `dto`                |
| `src/batteries.py`   | 21    | `service`            |
