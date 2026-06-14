# Product

<!-- truth: start -->
**Designing Performant APIs with Litestar** — a conference talk delivered as a
[Slidev](https://sli.dev/) deck for **EuroPython 2026, Kraków**.

- **What it is:** The presentation slides (and supporting Vue diagram components)
  for a ~30-minute technical talk on building Python APIs that stay fast as they
  grow — "by design, not by luck."
- **Who it's for:** EuroPython 2026 attendees — intermediate-to-advanced Python
  developers building or scaling web APIs. The artifact is the *deck*, not an app.
- **Speakers:** Cody Fincher (Litestar creator · Advanced Alchemy · SQLSpec) &
  Julien Courtès (CTO @ Laby · Litestar maintainer).
- **Differentiator:** Real, Shiki-highlighted Python code in-slide, a bespoke
  "Stellar Drift" Litestar theme, and custom Vue diagrams that visualize API
  complexity, the request pipeline, and layered configuration.

Session: <https://ep2026.europython.eu/session/designing-performant-apis-with-litestar>
<!-- truth: end -->

## Goals

- Tell a clear narrative: an API "looks small — until it isn't," and Litestar's
  design choices keep it performant and maintainable at scale.
- Keep code examples real, runnable-looking, and idiomatic Litestar.
- Deliver a visually polished, on-brand deck that exports cleanly to a static
  site and PDF for sharing after the talk.

## Non-Goals

- This repo is **not** a Litestar application. There is no API to run, deploy,
  or test here — only presentation content.
- No backend, database, or production infrastructure.

## Definition of Done (for this deck)

- The deck builds (`npm run build`) and exports to PDF (`npm run export-pdf`)
  without errors.
- Narrative flows slide-to-slide; speaker split (Cody/Julien) is correct.
- Code blocks render with correct Shiki highlighting and accurate Litestar APIs.
- Custom theme and Vue components render correctly in both dev and exported builds.
