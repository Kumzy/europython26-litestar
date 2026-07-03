import { defineShikiSetup } from '@slidev/types'

// Stellar Drift is always dark — pin a dark token theme for both color
// schemes so code never renders with light-theme tokens on the dark panels.
export default defineShikiSetup(() => {
  return {
    themes: {
      dark: 'tokyo-night',
      light: 'tokyo-night',
    },
  }
})
