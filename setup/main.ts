import { defineAppSetup } from '@slidev/types'

// The CLI exporter drives the play route with `?print=...` while emulating
// *screen* media, so `@media print` never applies during `slidev export`.
// Mirror the /print page behavior (it adds `print` to <html>) so styles can
// target export output with `html.print ...` — used to swap Acrobat-hostile
// CSS gradients for pre-rendered assets (see .agents/research/research_pdf_export).
export default defineAppSetup(() => {
  if (typeof window !== 'undefined' && new URLSearchParams(window.location.search).has('print')) {
    document.documentElement.classList.add('print')
  }
})
