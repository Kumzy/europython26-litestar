# Deck Review — Suggestions

Prepared 2026-07-14, the day before the talk. Constraints honored throughout:
**minimal changes only, no new slides, Litestar-centric framing.** Nothing below
has been applied except where marked done.

## Already applied

**Litestar 3 sweep across all example code (2026-07-14).** Three 3.0 changes
affect handler signatures, detected mechanically by running the tripwire tests
with `-W error::DeprecationWarning` under the pinned Litestar 2.24:

1. Implicit name-based DI → `NamedDependency[T]` (removed in 3.0)
2. Inferred path params → `FromPath[T]` (or `Annotated[T, PathParameter(...)]`)
3. Inferred query params → `FromQuery[T]` (or `Annotated[T, QueryParameter(...)]`)

Files updated:

- `slides/4.md` (inline, shown on stage) — `NamedDependency` on `user`/`db`,
  `FromQuery` on all five query params. The extra ceremony _helps_ this
  slide's "requirements pile up" story.
- `examples/src/orders.py` (slide 4's tripwire twin) — same change.
- `examples/src/controllers.py` (shown on slide 15) — `svc:
NamedDependency[OrderService]`.
- `examples/src/dtos.py` (shown on slide 19) — `order_id: FromPath[UUID]`.
- Already correct, untouched: `di.py`; nothing to change in `hello.py`,
  `blocking.py`, `batteries.py`.

Verified: pytest passes with deprecation warnings as errors (so no pre-3.0
idiom remains anywhere), `make lint` clean, `make build` clean. Displayed
snippet regions kept their line counts, so the click-highlight ranges on
slides 15 and 19 still line up.

## Recommended edits before tomorrow (smallest first)

1. **Slide 3 — visible typo** (`slides/3.md:6`): kicker reads
   `happy developper` → `happy developer`.
2. **Slide 4 — optional one word** (`slides/4.md`): `Session` → `AsyncSession`.
   A sync session inside `async def` quietly contradicts slide 18's own
   "one blocking call" lesson, and this is a maintainer audience.
3. **Slide 9 — sharpen the DI line** (`slides/9.md:16`): replace
   "Config & structure choices are limited; DI is global-ish" with
   **"No app-scoped DI — everything re-resolves per request."**
   It is more accurate, harder to rebut, and it sets up slide 17
   (lifecycles) as the payoff.
4. **Slide 13 — make the concern map match the slides that follow it**
   (`slides/13.md`, one array edit, still 5 rows / 5 clicks):

   | Concern                        | Litestar construct    | Delivered on |
   | ------------------------------ | --------------------- | ------------ |
   | Cross-cutting request behavior | Middleware & guards   | slide 14     |
   | Resource and route boundaries  | Controllers & routers | slides 15–16 |
   | Shared resources               | DI & lifespan         | slide 17     |
   | Response shaping               | DTOs                  | slide 19     |
   | External integrations          | Plugins               | slide 21     |

   Today the map lists Guards as its own row (no slide delivers it) and omits
   DTOs — the marquee feature — entirely. This reorder turns the map into the
   section's table of contents.

5. **Presenter notes** — only 5 of 23 slides have them. HTML-comment notes are
   zero render risk; worth adding the handoff cues tonight (see "Speaker split
   & handoff" below).

## Speaker split & handoff

Cody's instinct — Julien opens, Cody covers the details in the second half —
is the right one, and the deck already leans that way: slide 13 carries a
"Julien · 1:10" note and slide 21 a "Cody · 1:00" note. Recommended plan,
one primary handoff:

| Slides                         | Voice     | Why this voice                                                                                                                                                                                                            |
| ------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1–7 story                      | Julien    | The growing-API pain story is a _user's_ story — the CTO-running-Litestar-in-production voice makes it lived experience, not setup. Both intro on slide 1, then Julien takes the narrative.                               |
| 8–10 landscape                 | Julien    | "You usually pick one… or the other" is the user's dilemma; it rings truer from the person who had to choose than from the person who built the third option.                                                             |
| 11–13 philosophy               | Julien    | Slide 13's row-by-row concern map reveal ends as the table of contents for the second half — the perfect baton.                                                                                                           |
| **Handoff**                    | 13 → 14   | Every row on the map is a design decision, and Cody made them — e.g. _"…and each of these rows is a design choice. Cody made most of them, so he gets to defend them."_ The pass is narratively motivated, not arbitrary. |
| 14–20 building blocks + payoff | Cody      | Creator / design-intent voice ("we built it this way because…"); the blocking-call slide 18 also plays to the database background.                                                                                        |
| 21 ecosystem                   | Cody      | Advanced Alchemy and SQLSpec are his projects; matches the existing note.                                                                                                                                                 |
| 22–23 close                    | See below | Two options.                                                                                                                                                                                                              |

**Close — two options:**

- **A (simplest):** Cody straight through 22–23. One handoff all talk, lowest risk.
- **B (recommended if you rehearse it once):** Julien delivers slide 22's three
  takeaways as the production user's verdict — the claims land harder as
  testimony than as self-assessment — then Cody closes 23 with "Litestar 3 is
  coming," which belongs in the creator's voice. Slide 22 is three bullets;
  the extra handoff is cheap.

**Timing:** roughly 12 min Julien (1–13; the memes are seconds) and 13–14 min
Cody (14–23, the denser half) — balanced for a 30-minute slot with Q&A.

**Mechanics:** write the actual handoff sentence into the presenter notes of
slides 13 and 14 (and 21/22 if using option B). Fumbled passes are where
two-speaker talks lose energy; a scripted cue line each costs nothing.

## Keep as-is (deliberate, validated choices)

- **No benchmark slide.** Correct call. TechEmpower shipped its final round in
  Feb 2025 and was archived in March 2026 — and it never listed Litestar under
  its current name. Whole-framework req/s slides are the single most-attacked
  slide genre in framework talks. The architecture-first arc is what actually
  converts people (see James Bennett's "Litestar is worth a look," Aug 2025 —
  zero performance claims, HN front page).
- **Meme pacing (slides 5, 7).** Front-loaded levity before a dense middle is
  fine for 30 minutes; reordering the day before isn't worth the risk.
- **The landscape framing (slides 8–10).** Flask still ships no built-in
  validation/OpenAPI; Django 6.0's async ORM is still thread-wrapped with no
  async transactions. "Bring your own" and "you adopt the whole worldview"
  both hold as of July 2026.
- **Slide count and arc.** Problem story (2–7) → landscape (8–10) → design
  (11–19) → payoff (20) → ecosystem/close (21–23) matches the structure of the
  framework talks that historically landed (capability first, incremental
  adoption, no rewrite demand).

## Performance: what to claim on stage (verified)

Measured 2026-07-14 on this machine — identical 10-field order model,
identical 170 KB JSON output, 1000-object list, median of 300 runs:

| Encoder                              | Time     |                 |
| ------------------------------------ | -------- | --------------- |
| msgspec 0.21.1 (Litestar)            | 0.186 ms | **4.5x faster** |
| pydantic-core 2.13.4 Rust serializer | 0.842 ms |                 |

- **Safe claim:** "msgspec serializes several times faster than Pydantic's
  Rust core — and DTOs mean you only encode the fields you actually ship."
  Both halves verified; the serializer gap is the _floor_, since msgspec also
  handles request-side decoding/validation and DTOs shrink the payload itself.
- **Litestar is still faster.** Full stop. The only phrasing to skip is the
  mechanism claim "FastAPI serializes in slow pure Python" (its path changed
  in early 2026); the conclusion needs no update.
- If pressed for numbers in Q&A: msgspec's published benchmarks plus
  Litestar's own caveated harness (docs.litestar.dev/main/benchmarks.html) —
  quoting your own disclaimer is a credibility move. Repro script:
  `serializer_bench.py` (session scratchpad).

## Q&A preparation (verbal only, Litestar-centric)

- **"Why not just Starlette?"** — Slide 8 is the answer: you rebuild
  validation, serialization, DI, and OpenAPI on every project. Litestar is
  what "bring your own" looks like after someone brings it all, coherently.
- **"What about Django Ninja?"** — Nice ergonomics inside Django's worldview;
  the moment you need what slides 12–19 show (layered config, app-scoped DI,
  DTOs, guards), you're back to composing it by hand.
- **"FastAPI is adding per-router config."** — "Litestar was _designed_ around
  layering; others are retrofitting it" — then pivot to slide 12.
- **Community size** — answer with the ecosystem already on slide 21
  (Advanced Alchemy, SQLSpec, fullstack reference app, plugin protocols).
  Do not go near governance/bus-factor comparisons.
- Optional opener stat: FastAPI is now the most-used Python web framework
  (38%, JetBrains State of Python 2025) — "most of you are running it" is
  grounded, and makes the talk a gift rather than a pitch.

## First-party plugin coverage on slide 21 (verified 2026-07-14)

Checked every active repo on `litestar-org`, `cofin`, and `provinzkraut`
against the four ecosystem cards. The named list covers all the headliners:
Granian (Serve); Vite/Inertia + HTMX (Web); Advanced Alchemy, SQLSpec,
AsyncPG, OracleDB (Data); Queues, MCP, Emails (Work & integrate) — backed by
`litestar-granian`, `litestar-vite`, `litestar-htmx`, `litestar-asyncpg`,
`litestar-oracledb`, `litestar-queues`, `litestar-saq`, `litestar-mcp`,
`litestar-email`, plus the fullstack card.

**Released first-party plugins not represented:**

| Plugin                 | Home         | Status                                              | Card it fits     |
| ---------------------- | ------------ | --------------------------------------------------- | ---------------- |
| `litestar-django`      | litestar-org | v0.2.2, pushed May 2025                             | Data             |
| `litestar-piccolo`     | litestar-org | v0.1.0, pushed Nov 2024                             | Data             |
| `litestar-aiosql`      | cofin        | v0.1.2, pushed Sep 2024                             | Data             |
| `litestar-autowire`    | cofin        | v0.2.0, pushed Jul 2026                             | Work & integrate |
| `litestar-httpx-oauth` | cofin        | part of the offering (per Cody, despite quiet repo) | Work & integrate |

Deliberately skipped: `litestar-oidc` (WIP, no release) and
`litestar-socketify` (dormant since 2023; the Serve card's "any ASGI server
works" already covers its niche). Note: no public Litestar plugin
repos exist on `provinzkraut`'s personal account as of today — whatever is
staged there is either private or already moved to the org.

**Applied:** slide 21's Work & integrate card now reads
"Queues, MCP, Emails, **OAuth**, etc" (covers `litestar-httpx-oauth`).

**Recommendation (one small edit, or none):** the slide's own presenter note
says "map, not a feature checklist," and the cards end in "etc" — so strictly,
nothing else is wrong. The one remaining name worth adding is
**`litestar-django`** on the Data card: it's org-level, released, and "bring
your Django models to Litestar" is a bridge-builder line for the Django
contingent at a Python conference. Piccolo/aiosql stay under "etc".

## Logistics

- **Jacob Coffee presents "Supercharging Litestar: Extensibility Through
  Plugins" at EP2026 on Thursday July 16** — the day after you. On slide 21,
  a verbal cross-reference ("for plugin depth, Jacob's talk Thursday") turns
  overlap into a funnel.
- **Slide 23 QR** still points at the Discord (known TODO in the file). If the
  deck URL isn't hosted by tonight, the Discord is an acceptable fallback —
  just say so when you gesture at it.
- The EP2026 program lists the session as **Beginner** level: the story arc on
  slides 3–7 earning its runtime is a feature — don't rush it.
