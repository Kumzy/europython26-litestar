<script setup lang="ts">
// Slide 6 (right): complexity over time — click-revealed, in order:
// X axis (label lands after the draw) → Y axis (same) → "by luck" (explodes)
// → "vibe-coded 🤖" (explodes from day one) → "the dream" (flat fantasy)
// → "by design" (kept low — the talk's promise, lands last).
// Lines draw in left-to-right via stroke-dashoffset on their v-click reveal.
</script>

<template>
  <svg
    class="journey"
    viewBox="0 0 360 240"
    role="img"
    aria-label="Complexity over time: exploding by luck, low by design, flat in the dream"
  >
    <!-- 1. X axis: draws from the origin, "Time" label lands when it finishes -->
    <g v-click>
      <line class="axis axis-x" x1="34" y1="196" x2="344" y2="196" />
      <path class="axis-head axis-head-x" d="M342 191 L 350 196 L 342 201 Z" />
      <text class="cap cap-x" x="190" y="224" text-anchor="middle">Time</text>
    </g>

    <!-- 2. Y axis: grows upward, "Complexity" label lands when it finishes -->
    <g v-click>
      <line class="axis axis-y" x1="34" y1="196" x2="34" y2="16" />
      <path class="axis-head axis-head-y" d="M29 18 L 34 10 L 39 18 Z" />
      <text class="cap cap-y" x="22" y="105" text-anchor="middle" transform="rotate(-90 22 105)">
        Complexity
      </text>
    </g>

    <!-- 3. by luck: complexity explodes -->
    <g v-click>
      <path class="curve luck" d="M40 186 C 150 180, 250 140, 318 26" />
      <text class="lbl luck-t" x="344" y="24" text-anchor="end">by luck 🔥</text>
    </g>

    <!-- 4. vibe-coded by the manager: explodes from day one -->
    <g v-click>
      <path class="curve vibe" d="M40 186 C 52 110, 62 42, 72 16" />
      <text class="lbl vibe-t" x="82" y="24" text-anchor="start">vibe-coded 🤖</text>
    </g>

    <!-- 5. the dream: flat forever -->
    <g v-click>
      <path class="curve dream" d="M40 186 L 340 186" />
      <text class="lbl dream-t" x="344" y="176" text-anchor="end">the dream ✨</text>
    </g>

    <!-- 6. by design: kept as low as possible — the talk's promise, lands last -->
    <g v-click>
      <path class="curve design" d="M40 186 C 140 178, 240 168, 340 148" />
      <text class="lbl design-t" x="344" y="138" text-anchor="end">by design</text>
    </g>
  </svg>
</template>

<style scoped>
.journey {
  width: 100%;
  max-width: 420px;
  height: auto;
  font-family: 'Inter', sans-serif;
}
.axis {
  stroke: var(--ls-muted);
  stroke-width: 1.5;
}
.axis-head {
  fill: var(--ls-muted);
}
.curve {
  fill: none;
  stroke-width: 3;
  stroke-linecap: round;
}
.luck {
  stroke: var(--ls-orange);
}
.vibe {
  stroke: var(--ls-violet);
}
.vibe-t {
  fill: var(--ls-violet);
}
.design {
  stroke: var(--ls-mint);
}
.dream {
  stroke: var(--ls-gold);
  stroke-dasharray: 7 7;
}
.lbl {
  font-size: 12px;
  font-weight: 800;
}
.luck-t {
  fill: var(--ls-orange);
}
.design-t {
  fill: var(--ls-mint);
}
.dream-t {
  fill: var(--ls-gold);
}
.cap {
  fill: var(--ls-muted);
  font-size: 11px;
  font-style: italic;
}

/* axes draw in sequence on their reveal: X from the origin, then Y grows up */
g.slidev-vclick-target .axis-x {
  stroke-dasharray: 310;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 450ms ease;
}
g.slidev-vclick-hidden .axis-x {
  stroke-dashoffset: 310;
}
g.slidev-vclick-target .axis-y {
  stroke-dasharray: 180;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 450ms ease;
}
g.slidev-vclick-hidden .axis-y {
  stroke-dashoffset: 180;
}
g.slidev-vclick-target .axis-head-x,
g.slidev-vclick-target .axis-head-y {
  opacity: 1;
  transition: opacity 200ms ease 400ms;
}
g.slidev-vclick-hidden .axis-head-x,
g.slidev-vclick-hidden .axis-head-y {
  opacity: 0;
}
/* axis labels land once their axis has finished drawing */
g.slidev-vclick-target .cap-x,
g.slidev-vclick-target .cap-y {
  opacity: 1;
  transition: opacity 250ms ease 500ms;
}
g.slidev-vclick-hidden .cap-x,
g.slidev-vclick-hidden .cap-y {
  opacity: 0;
}

/* draw each line left-to-right when its click fires */
g.slidev-vclick-target .curve {
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 800ms ease;
}
g.slidev-vclick-target .luck,
g.slidev-vclick-target .vibe,
g.slidev-vclick-target .design {
  stroke-dasharray: 700;
}
g.slidev-vclick-hidden .luck,
g.slidev-vclick-hidden .vibe,
g.slidev-vclick-hidden .design {
  stroke-dashoffset: 700;
}
/* dream line: wipe in left-to-right so the dash pattern stays put */
g.slidev-vclick-target .dream {
  clip-path: inset(-6px -6px -6px -6px);
  transition: clip-path 800ms ease;
}
g.slidev-vclick-hidden .dream {
  clip-path: inset(-6px 100% -6px -6px);
}
</style>
