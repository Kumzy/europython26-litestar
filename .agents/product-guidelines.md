# Product Guidelines

Brand, tone, and visual guidelines for the deck. The bespoke theme lives in
`styles/main.css` (the "Stellar Drift" Litestar theme).

## Tone of Voice

- **Confident and practical**, not academic. Speak to working engineers.
- **Narrative-driven**: every section advances the "small API → production
  reality" story. Avoid bullet dumps where a sentence or diagram works better.
- **Honest about trade-offs.** Show why Litestar's design choices pay off, but
  don't oversell. Credibility with a developer audience comes from nuance.
- Short, punchy slide titles. The lead/sub-text carries the nuance.

## Visual Style — "Stellar Drift"

- **Theme base:** Slidev `default` theme, heavily overridden by `styles/main.css`.
- **Motifs:** five-point star (`Star.vue`), gold accent (`.gold`), "kicker"
  eyebrow labels above titles (`.kicker`), card and divider treatments.
- **Fonts:** `Inter` (sans), `JetBrains Mono` (mono). Do not swap fonts ad hoc.
- **Code:** Shiki highlighter. Code blocks are *real* Python — keep them
  accurate and idiomatic, with line highlighting/transitions used purposefully,
  not decoratively.
- **Diagrams:** prefer the custom Vue components over static images:
  - `StackCompare.vue` — "what we think we build vs. production reality" hook.
  - `JourneyCurve.vue` — complexity-up / velocity-down chart.
  - `MiddlewareChain.vue` — request → handler pipeline.
  - `LayerConfig.vue` — app / router / controller / handler cascade.
  - `EventLoop.vue` — one-lane event loop stalled by a blocking call.
  - `Star.vue` — the five-point star motif.

## Constraints

- **Consistency first.** Reuse existing CSS classes (`.kicker`, `.lead`,
  `.gold`, `.muted`, card/divider styles) before introducing new ones.
- **16:9 canvas**, readable from the back of a conference room: large type,
  high contrast, minimal text per slide.
- The former placeholder graphics are now Vue components: the "what we build vs.
  reality" stack (`StackThink`/`StackReality`, slide 2) and the layered-config
  cascade (`LayerConfig`, slide 14). The one open placeholder is the slide 22 QR
  (`public/qr.svg`), still the Discord link — swap for the hosted deck URL.
- Speaker attribution and bios are on slides 1 and 22 — keep them accurate.
- Exported artifacts (static site + PDF) must look identical to the live deck.
