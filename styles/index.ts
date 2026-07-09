// Static font instances (not the Google variable fonts): Chromium's
// print-to-PDF embeds static fonts as TrueType subsets, while variable fonts
// get flattened into Type 3 vector glyphs that Acrobat renders poorly.
// Keep every weight used in main.css / components; missing weights would be
// synthesized and re-introduce Type 3 output in the exported PDF.
import '@fontsource/inter/200.css'
import '@fontsource/inter/400.css'
import '@fontsource/inter/400-italic.css'
import '@fontsource/inter/500.css'
import '@fontsource/inter/600.css'
import '@fontsource/inter/700.css'
import '@fontsource/inter/800.css'
import '@fontsource/inter/900.css'
import '@fontsource/jetbrains-mono/400.css'
import '@fontsource/jetbrains-mono/400-italic.css'
import '@fontsource/jetbrains-mono/500.css'
import '@fontsource/jetbrains-mono/700.css'
import '@fontsource/jetbrains-mono/800.css'

import './main.css'
