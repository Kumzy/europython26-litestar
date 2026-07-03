import { defineShikiSetup } from '@slidev/types'

//https://github.com/shikijs/textmate-grammars-themes/tree/main/packages/tm-themes
export default defineShikiSetup(() => {
  return {
    themes: {
      dark: 'github-dark',
      light: 'github-dark',
    },
  }
})
