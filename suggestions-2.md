# Deck Review 2 — Flow, Tone, and Speaker Phrasing

Prepared 2026-07-15 for review. **Proposal only: none of these changes have
been applied to the deck.** The goal is to improve narrative flow and
co-speaker dialogue while avoiding performance boasting, framework bashing,
or claims that sound broader than the evidence.

Constraints:

- no new slides;
- preserve the existing story and speaker split;
- describe Litestar's design strengths without declaring a framework winner;
- prefer predictable, explicit, scoped, and measurable over fast or faster;
- distinguish isolated measurements from end-to-end application performance;
- describe framework capability as a sliding scale; do not use "batteries" as
  a binary category that groups FastAPI and Django together.

## Core framing

Use this as the talk's central idea:

> Good performance comes from making cost and scope explicit.

Use this as the Litestar-specific claim:

> Litestar gives you clear places to express those decisions.

Do **not** make framework superiority the thesis. The talk should argue that
performance survives growth when teams can see where work runs, how often it
runs, and which boundary owns it.

## Exact visible-copy adjustments

### Slides 8–10 — use a sliding scale, not two opposing camps

The current sequence places Flask/Starlette at one end and FastAPI/Django at
the other. That collapses materially different frameworks into two categories.
Use four distinct positions instead:

1. **Flask / Starlette:** HTTP foundations and core primitives;
2. **FastAPI:** schema validation, serialization, OpenAPI, and DI, while
   leaving many application and integration choices open;
3. **Litestar:** a broader set of integrated capabilities, organized around
   layered and replaceable boundaries;
4. **Django:** a fuller application stack with ORM, auth, admin, forms,
   templates, migrations, and strong shared conventions.

This is not a quality ranking. It describes how much of the application stack
each framework chooses to provide.

### Slide 8 — foundations

Replace kicker:

> Low-level

With:

> Foundations

Replace title:

> Flask / Starlette - minimalist

With:

> Flask / Starlette - core web primitives

Keep:

> Maximum flexibility, minimal assumptions

Replace:

> You rebuild the same plumbing on every project

With:

> You assemble validation, serialization, DI, and OpenAPI yourself

Replace:

> Performance is on you — easy to get subtly wrong

With:

> Performance depends on how those pieces are selected and composed

Reason: this preserves the tradeoff while treating Flask and Starlette as
deliberate choices rather than incomplete frameworks.

### Slide 9 — give FastAPI and Django distinct positions

Replace kicker:

> High-level & opinionated

With:

> A sliding scale

Replace title:

> FastAPI / Django - opinionated

With:

> Frameworks provide different parts of the stack

Replace the current FastAPI and Django lists with this exact copy:

> **FastAPI**
>
> - Validation, serialization, OpenAPI, and dependency injection
> - Deliberately leaves many application and integration choices to you
>
> **Django**
>
> - ORM, auth, admin, forms, templates, migrations, and more
> - A fuller application stack with shared conventions

Replace the right-column conclusion with:

> **This is a continuum, not two camps.**
>
> Each framework chooses a different boundary between what it provides and
> what the application assembles.
>
> **The useful question:** which decisions are provided, and which remain
> yours?

Reason: FastAPI provides important API-layer capabilities but is comparatively
unopinionated about the rest of the application. Django provides a much fuller
stack. Treating them as equivalent obscures the actual design tradeoff.

### Slide 10 — draw four positions on the spectrum

Replace title:

> You usually pick one… or the other

With:

> Framework capability is a sliding scale

Replace the current three spectrum positions with four positions using this
exact label and sublabel copy:

> **Flask / Starlette**
>
> HTTP foundations — assemble the rest
>
> **FastAPI**
>
> validation, OpenAPI & DI — choose most integrations
>
> **Litestar**
>
> broader built-in capabilities — layered & replaceable
>
> **Django**
>
> full application stack — shared conventions

Replace the closing question with:

> How much should the framework provide — and where can you override it?

Reason: the four positions communicate the intended model directly. Litestar
is one design point on the scale, not an escape from a false binary.

### Slide 11 — tighten the definition heading

Replace:

> "Composable" - What we actually mean?

With:

> "Composable" — what do we actually mean?

Replace:

> All the batteries are there: DI, validation, OpenAPI, plugins

With:

> Built-in capabilities include DI, validation, OpenAPI, and plugin protocols

Replace:

> And every one is optional: bring your own and plug it in at any level

With:

> Each boundary is replaceable: use the built-in or integrate your own

Reason: naming the capabilities is clearer than using "batteries" as a generic
label, and it keeps the continuum established on slides 8–10 intact.

### Slide 18 — avoid an absolute outcome

Replace title:

> One blocking call stalls every request behind it

With:

> One blocking call can stall every request behind it

Replace the visible conclusion:

> Litestar won't guess: an undeclared sync handler is a startup warning, not a
> production mystery.

With:

> Litestar makes the choice explicit: an undeclared sync handler produces a
> startup warning.

Replace this presenter-note line:

> The consequence: every request queued behind that read_csv waits.

With:

> The consequence: requests queued behind that read can be delayed.

Replace the presenter-note conclusion:

> The design point: Litestar refuses to guess. A sync handler that doesn't
> declare sync_to_thread is a warning at startup — the decision is always
> explicit, never implicit.

With:

> The design point: Litestar keeps the choice explicit. A sync handler without
> sync_to_thread produces a startup warning, making the execution model visible
> before serving traffic.

### Slide 19 — make the serialization claim conditional

Replace:

> Serialized by msgspec in one pass, can use any library (python dict,
> Pydantic, etc)

With:

> Use msgspec or another supported type; measure with your own payloads

Suggested spoken expansion:

> Narrow DTOs can reduce serialization work because fewer fields cross the
> wire. The actual gain depends on the model, payload, and workload.

### Slide 20 — change the payoff from a boast to a diagnostic summary

Replace title:

> Common pitfalls, designed away

With:

> Common performance costs, made visible

Replace row 3's measurement:

> a fresh HTTP client: ~8 ms/request → 0

With:

> reuse clients and pools across requests

Replace row 4's measurement:

> 30 fields vs the 5 you need: ~5× encode cost

With:

> encode only the fields the client needs

Replace the presenter-note close:

> True in any framework, Litestar just makes the fix the default path.

With:

> These principles apply in any framework. Litestar gives each one an
> explicit place in the application structure.

Reason: the existing numbers are workload-dependent and appear without the
methodology on the slide. Removing them strengthens credibility without
weakening the architectural point.

### Slide 21 — call ecosystem entries integrations, not batteries

Replace the Data card sentence:

> Advanced Alchemy, SQLSpec, and Django - first-party batteries, fully
> supported.

With:

> Advanced Alchemy, SQLSpec, and Django - supported first-party data
> integrations.

Make the same terminology change in the presenter note and in the applied-edit
summary in `suggestions.md`.

### Slide 23 — refine the takeaways

Replace takeaway 1:

> High-level, so you don't rebuild plumbing

With:

> Capable, so common API concerns are already integrated

Replace takeaway 3:

> Layered & explicit, so performance stays predictable

With:

> Layered & explicit, so performance costs stay visible

## Exact spoken flow

These lines belong in presenter notes, not visible slide copy.

### Slides 1 → 2 — establish the contract

After introductions, Julien:

> This is not a benchmark talk. It is about keeping performance understandable
> as an API, a team, and its requirements grow.

Then, on slide 2:

> The first endpoint is rarely the problem. The problem is all the work that
> gathers around it over time.

### Slides 7 → 8 — introduce alternatives fairly

Julien:

> Think of this as a sliding scale, not two camps. Flask and Starlette provide
> the HTTP foundations. FastAPI adds validation, OpenAPI, and dependency
> injection while leaving many other choices open. Django provides much more
> of the application stack. Each is a deliberate design point.

### Slides 10 → 11 — turn the claim into a question

Julien:

> Litestar occupies another point on that scale. Its answer depends on the word
> "composable," so let us define that before we claim it.

### Slides 12–20 — recurring connective phrase

Use this phrase selectively, no more than three times:

> Scope determines how often work runs.

Suggested placements:

- slide 12: after explaining the highest owning layer;
- slide 17: when contrasting app and request lifetimes;
- slide 20: as the summary of the five costs.

This phrase connects the architecture section back to performance without
claiming Litestar is universally faster.

### Slides 13 → 14 — primary handoff

Julien:

> Those are the boundaries. Cody, show us how Litestar represents them in a
> request.

Cody:

> Let us start with the request pipeline.

Reason: this sounds like the next part of one explanation, rather than a
formal transfer of the stage.

### Slides 17 → 18 — connect scope to event-loop behavior

Cody:

> Correct scope prevents unnecessary work. The next question is whether the
> work we do need can block everything else.

### Slides 19 → 20 — introduce the payoff

Cody:

> None of these choices guarantees a fast application. They make the costs
> visible enough to measure, reason about, and change.

### Slides 22 → 23 — closing handoff

Cody:

> Julien, what should people take back to their teams?

Julien:

> Three things.

After the third takeaway, Julien:

> That is the design. Cody, where should people start?

### Slide 24 — practical call to action

Cody:

> The QR has the deck and the code. Take the patterns, measure them in your own
> application, and come tell us what you find. Litestar 3 is coming, but you
> can use these design ideas today.

Reason: the audience leaves with an action rather than an unsupported claim of
framework superiority.

## Corrections to the original review language

When this proposal is approved, update the older `suggestions.md` wording as
well so it does not preserve the binary framing after the slides change.

### Landscape summary

Replace:

> "Bring your own" and "you adopt the whole worldview" both hold as of July 2026.

With:

> Framework capability is a sliding scale. Flask and Starlette provide core
> web primitives; FastAPI adds schema validation, OpenAPI, and DI while leaving
> many application choices open; Django provides a fuller application stack
> with stronger shared conventions.

### “Why not just Starlette?” Q&A

Replace:

> You rebuild validation, serialization, DI, and OpenAPI on every project.
> Litestar is what "bring your own" looks like after someone brings it all,
> coherently.

With:

> Starlette is a strong foundation when you want to select and assemble those
> pieces yourself. Litestar provides more of them together, with layered
> configuration and explicit replacement points.

### “What about Django Ninja?” Q&A

Replace:

> Nice ergonomics inside Django's worldview; the moment you need what slides
> 12–19 show, you're back to composing it by hand.

With:

> Django Ninja is a strong choice when you want Django's application stack with
> a type-driven API layer. Litestar is aimed at teams that want broader API
> capabilities without adopting the full Django stack.

### “FastAPI is adding per-router config” Q&A

Replace:

> Litestar was designed around layering; others are retrofitting it.

With:

> Different frameworks draw configuration boundaries differently. Layered
> configuration has been central to Litestar's model, and the practical
> question is whether that model fits the scopes in your application.

## Performance Q&A phrasing

Do not volunteer the isolated serializer comparison in the main talk. If
asked directly, use:

> In our isolated serializer check, msgspec was faster for that specific
> payload. End-to-end API performance also includes validation, middleware,
> I/O, database work, payload shape, and deployment. The useful answer is to
> measure your workload.

Replace the sentence from the first review:

> Litestar is still faster. Full stop.

With:

> Litestar is designed to keep common costs explicit and gives you efficient
> defaults. Whether an application is faster depends on the workload and how
> it is built.

If asked why Litestar uses msgspec:

> msgspec is an efficient default and integrates well with Litestar's DTO
> pipeline. The larger design point is that the serialization boundary is
> explicit and replaceable.

## Pacing and conversational rhythm

### Slide 6

It currently contains roughly ten reveals. Deliver it as three spoken beats:

1. prototype and MVP success;
2. accumulated production costs;
3. the inherited demo punchline.

Do not pause after every reveal. The slide should accelerate into the joke,
not feel like a checklist.

### Slide 21

Treat the ecosystem as a map and keep it under one minute. Name one example
per card, then let the slide carry the rest. The key sentence is:

> The same plugin boundary supports each of these shapes; the list itself is
> less important than the extension point.

### Timing checkpoints

- reach slide 7 by approximately minute 5;
- reveal Litestar on slide 10 by minute 8 or 9;
- make the primary handoff at slide 14 around minute 12;
- reach the payoff on slide 20 around minute 22;
- begin the recap on slide 23 around minute 25;
- finish by minute 26, preserving roughly four minutes for questions.

## Approval checklist

- [ ] Approve the four-position sliding scale on slides 8–10.
- [ ] Approve matching corrections to the original review's landscape and Q&A
      wording.
- [ ] Approve conditional performance wording on slides 18–20.
- [ ] Approve "performance costs stay visible" on slide 23.
- [ ] Approve the opening thesis and recurring scope phrase.
- [ ] Approve the revised speaker handoffs and close.
- [ ] Approve removal of uncited workload-specific numbers from slide 20.
- [ ] Approve pacing guidance only; no click changes unless rehearsal shows a
      problem.
