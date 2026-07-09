# Research: PDF export "not working correctly"

**Workspace**: `.agents/research/research_pdf_export/`
**Status**: Complete
**Type**: Bug Investigation
**Date**: 2026-07-08

## Executive Summary

**User-clarified symptom (2026-07-08):** the PDF is heavy, slow to load, and
renders badly in Adobe Acrobat. Root causes found, fixed, and measured —
**5.2MB → 601KB (8.7×)**:

- **Heavy (83% of the file):** `public/lady-thinking-meme.png` (slide 7) was a
  1.7MB lossless PNG of photographic content; Chromium re-embeds PNGs as raw
  Flate rasters, ballooning it to **4.3MB inside the PDF**. Fixed by converting
  to an optimized JPEG (219KB on disk, visually identical in the export).
- **Bad Acrobat rendering + slow paint:** Google Fonts now serves Inter and
  JetBrains Mono **only as variable fonts** (verified: css2 returns the same
  variable woff2 for every requested weight). Chromium's print-to-PDF cannot
  subset variable fonts as TrueType, so it flattened all text into **90 Type 3
  vector fonts / 1,200 glyph-drawing programs / 1,344 content streams** — the
  known cause of fuzzy, heavy, slow text in Acrobat (plus synthesized faux
  weights like `Inter-Regular_SemiBold`). Fixed by self-hosting **static**
  weights via `@fontsource/inter` + `@fontsource/jetbrains-mono` with
  `fonts.provider: none`; the export now embeds clean **CID TrueType subsets**
  (real Bold/ExtraBold/Italic instances). Type 3 count: 90 → 12 (only ✓/emoji
  system-font fallbacks remain — unavoidable, color-emoji can't embed as
  TrueType). Bonus: fonts are bundled, so the deck no longer depends on Google
  Fonts at talk time.
- **Also found: artifact clobbering.** `slidev build` empties `dist/`, deleting
  `dist/slides.pdf` — the export silently vanishes on the next `make build`.
  Workflow fix recommended (build → export ordering or `download: true`).
- The rendering pipeline itself was verified healthy: all 23 pages correct at
  the pixel level across poppler-splash, poppler-cairo, Quartz (Preview), and
  PDFium (Chrome), before and after the fix. An early "light-mode page 18"
  suspicion was disproven (preview-tooling artifact, not the PDF).

## Research Tasks Summary

| Task | Status | Key Findings |
|------|--------|--------------|
| Reproduce export | Complete | `npm run export-pdf` succeeds; 23/23 pages present |
| Page-by-page verification | Complete | All pages correct (text extraction + visual sweep + pixel medians) |
| Renderer differential (poppler/Quartz/PDFium) | Complete | Identical, correct output in all engines |
| Browser vs export comparison | Complete | Dev server, `/print` route (screen + print media) all correct |
| PDF internals (fonts, links, graphics state) | Complete | Type 3 variable-font embedding; links preserved; opaque fills confirmed |
| Artifact lifecycle | Complete | **`slidev build` wipes `dist/slides.pdf`** |

## Codebase Analysis

### Key Locations

| File | Lines | Purpose |
|------|-------|---------|
| `Makefile` | 72–82 | `build` and `export-pdf` targets — both write into `dist/` |
| `package.json` | 8–10 | `build` → `slidev build`; `export-pdf` → `slidev export --format pdf --output dist/slides.pdf` |
| `slides.md` | 1–21 | Deck headmatter: `colorSchema: dark`, fonts `Inter`/`JetBrains Mono` (Slidev Google-Fonts provider → variable fonts) |
| `slides/18.md` | 10, 16, 23 | `<EventLoop />` + `<<< @/examples/src/blocking.py` snippets (the page most scrutinized) |
| `components/EventLoop.vue` | 1–84 | Static, scoped-styles component — exonerated |
| `styles/main.css` | 26–31, 189–191 | Unconditional dark backgrounds (`--ls-bg`, `pre` `#0e0b22 !important`) — render correctly in export |

### The failure chain (root cause)

1. `make export-pdf` (`Makefile:78-82`) writes `dist/slides.pdf`.
2. `make build` (`Makefile:72-76`) runs `slidev build`, which **cleans `dist/`
   before emitting the static site** — `dist/slides.pdf` is deleted (verified
   empirically: file present before build, gone after).
3. Since a clean `make build` is the documented verification gate
   (`CLAUDE.md`, `.agents/workflow.md`), the PDF is routinely destroyed after
   export, making the export appear broken/absent.

### Verification evidence

- Text extraction (pypdf): all pages have expected text; page 5 has none because
  it is the full-bleed image slide (`slides/5.md`, `layout: image`) — expected.
- Visual sweep of all 23 pages at 100 DPI: correct theme, layouts, diagrams,
  final-click state (right column of slide 18 visible, StackReality on slide 2
  visible — both correct default export behavior).
- Pixel medians of slide 18 regions across `pdftoppm`, `pdftocairo`,
  Quartz (`CGContextDrawPDFPage`), PDFium (`pypdfium2`): identical
  `leftPanel=(14,11,34)`, `rightPanel=(14,11,34)`, `laneBg=(27,22,64)`,
  `pageBg=(19,16,43)` — the exact theme colors.
- `pikepdf` graphics-state simulation: all panel fills painted at effective
  alpha 1.0 (an early alpha-leak hypothesis was disproven).
- Link annotations preserved: page 21 → litestar-fullstack GitHub, page 23 →
  litestar.dev.
- `--per-slide` export also correct (kept as a troubleshooting option only).

## Library Documentation

### Slidev (`@slidev/cli` ^52.16.0)

- Export requires `playwright-chromium` (present in `devDependencies`) —
  reference: `.agents/skills/slidev/references/core-exporting.md`.
- Default export = one page per slide at final click state; `--with-clicks` for
  per-click pages; `--per-slide` isolates per-slide capture (workaround for
  global-layer state issues).
- **`slidev build --download` / headmatter `download: true`** builds the static
  site *with* an exported PDF bundled — the supported way to get both artifacts
  from one command (reference: `references/build-pdf.md`).

### Chromium `page.pdf()` font embedding (background for observations)

- Variable fonts (Inter and JetBrains Mono webfonts are variable) are embedded
  as **Type 3 vector fonts** with synthesized instance names
  (`Inter-Regular_SemiBold`, `JetBrainsMono-Regular_wght…`). Text remains
  extractable (ToUnicode maps present) but files are larger and some tools warn.
- Poppler's "Bad bounding box in Type 3 glyph" warning is a known, noisy,
  float-rounding-prone sanity check ([Debian xpdf report](https://groups.google.com/g/linux.debian.bugs.dist/c/4-7JUlYp4bQ),
  [ghostscript #690882](https://bugs.ghostscript.com/show_bug.cgi?id=690882)) —
  benign here (rendering verified correct).
- Glyphs missing from the loaded webfont subsets (✓, →, ❌/✅) fall back to
  **local system fonts** — `.SFNS-Bold` and `AppleColorEmoji` on macOS — so the
  PDF's exact glyph shapes depend on the machine that ran the export.

## Prior Art

### Internal
- `CLAUDE.md` / `.agents/patterns.md` already note "PDF export (`make export-pdf`)
  needs `playwright-chromium`" — no prior record of the `dist/` clobbering.
- `make clean` (`Makefile:51-56`) also removes `dist/` — expected, documented.

### External
- Slidev's own solution for "site + PDF" is `slidev build --download`
  (bundles the PDF into the build output rather than exporting separately).
- Static (non-variable) font files are the standard remedy when Type 3
  embedding or fallback glyphs are unacceptable for a print artifact.

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Exported PDF silently deleted by `make build` (CI or local) | High | Med | Reorder/decouple artifacts (see Recommended Approach) |
| Export run on different OS (CI) yields different fallback glyphs (✓ → ❌/✅ emoji) | Med | Low | Export the final deliverable from one blessed machine, or self-host static fonts covering those glyphs |
| Poppler-based viewers/tools flag Type 3 warnings (noise in CI logs) | Med | Low | Ignore; verified benign. Optionally switch to static font files to eliminate |
| Slide 5 / 7 (image slides) have no extractable text (searchability/a11y of the shared PDF) | Low | Low | Acceptable for memes; add alt text in speaker notes if desired |

### Recovery Strategy

**Rollback Plan:** All proposed fixes are Makefile/frontmatter-only; revert the
commit to restore current behavior. No slide content changes required.
**Checkpoints:** `make build` + `make export-pdf` + open PDF after each change;
re-verify page count (23) and spot-check pages 2, 6, 18, 23.

## Applied Fix (in working tree, 2026-07-08)

| Change | File | Effect |
|--------|------|--------|
| Meme PNG → optimized JPEG (q82, progressive) | `public/lady-thinking-meme.jpg` (+`slides/7.md:3`), PNG deleted | PDF: 5.2MB → 1.12MB |
| Static fonts via Fontsource, all used weights (Inter 200/400/400i/500/600/700/800/900; JBM 400/400i/500/700/800) | `styles/index.ts`, `package.json` | PDF: 1.12MB → 601KB; Type 3 90 → 12; text embeds as CID TrueType → crisp/fast in Acrobat |
| Disable Google Fonts provider | `slides.md` headmatter `fonts.provider: none` | No variable fonts, no network dependency at runtime |

Verified: `npm run lint` + `oxfmt` clean, `make build` clean, re-export = 601KB /
23 pages, sample pages (1, 7, 18) pixel-checked. **Note:** any *new* font-weight
used in CSS must also be imported in `styles/index.ts`, or Chromium will
synthesize it and re-introduce Type 3 output.

## Acrobat Glitch Fix (applied 2026-07-09)

**Symptom (user):** Acrobat glitches, freezes briefly on page switches, and the
background paints in visible stages. **Cause:** Chromium print converts every
CSS gradient into a PDF tiling/shading pattern; the deck shipped **126 of
them**, mostly full-page transparent fills — the "Stellar Drift" starfield
(5 radial-gradients × every slide, `styles/main.css:51`), the cover glows
(2 × pages 1/23), and `LayerFlow`'s animated `repeating-linear-gradient`
dashes (5 full-canvas patterns on page 15). Acrobat composites stacked
transparent patterns per paint, hence the staged background drawing and
per-page freezes. Other viewers (Preview, Chrome) cope.

**Fix (patterns: 126 → 2 tiny chip fills on page 2):**

| Change | File | Mechanism |
|--------|------|-----------|
| Starfield → single inline SVG (5 `<circle>` dots) | `styles/main.css` `.slidev-layout::before` | SVG circles export as plain vector fills, no patterns; visually identical on screen |
| Cover glows → pre-rendered `public/cover-glow.png` (45KB, 735×414), **export only** | `styles/main.css` `html.print .ls-cover` | Screen keeps the crisp CSS gradients |
| LayerFlow dashes → real dashed borders, **export only** | `components/LayerFlow.vue` `html.print .vline/.hline` | Screen keeps the animated gradient dashes |
| `html.print` hook | `setup/main.ts` | The CLI exporter emulates **screen** media (`export-*.mjs`: `emulateMedia({media:'screen'})`), so `@media print` never fires; the play route with `?print=` sets no class either. The setup mirrors the `/print` page, which adds `print` to `<html>` |

**Rule for future styling:** avoid large-area CSS gradients (incl.
`repeating-linear-gradient`) on things that reach the exported PDF; use inline
SVG shapes, pre-rendered images, or `html.print` overrides. `.ls-section`
still carries a gradient (currently unused) — convert it if it gets adopted.

## Artifact Lifecycle Fix (applied 2026-07-09)

`slidev build` wipes `dist/`, which used to delete `dist/slides.pdf`. Fixed by
making `export-pdf` depend on `build` (`Makefile:79`): the export always runs
after the wipe, so `dist/` ends up with the static site *and* the PDF. Running
`make build` alone still removes a previously exported PDF — re-run
`make export-pdf` when you need both.

## Open Questions

- What exactly did the user observe (missing file vs. visual defect, and in
  which viewer)? The clobbering explains a missing/stale PDF; if they saw a
  *visual* defect in a specific viewer, capture the viewer + page number.
- Should the conference deliverable pipeline (final PDF for attendees) run on a
  single blessed environment to freeze fallback glyphs?

## Research Outputs

**This research informs:**
- PRD: `.agents/specs/{prd_id}/prd.md` (when created)
- Flow: `.agents/specs/{flow_id}/` (when created)
