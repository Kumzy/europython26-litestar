<script setup lang="ts">
// Slide 5: as endpoints pile up, complexity climbs while velocity drops.
// Two curves crossing — the moment momentum is lost.
</script>

<template>
  <svg
    class="journey"
    viewBox="0 0 360 240"
    role="img"
    aria-label="Complexity rising, velocity falling over time"
  >
    <!-- axes -->
    <line class="axis" x1="34" y1="14" x2="34" y2="196" />
    <line class="axis" x1="34" y1="196" x2="346" y2="196" />

    <!-- complexity: rising -->
    <path class="curve complexity" d="M40 184 C 120 176, 210 150, 340 30" />
    <!-- velocity: falling -->
    <path class="curve velocity" d="M40 44 C 150 70, 230 150, 340 188" />

    <!-- crossover -->
    <circle class="cross" cx="196" cy="120" r="5" />

    <!-- end labels -->
    <text class="lbl complexity-t" x="344" y="26" text-anchor="end">Complexity</text>
    <text class="lbl velocity-t" x="344" y="204" text-anchor="end">Velocity</text>

    <!-- axis captions -->
    <text class="cap" x="190" y="224" text-anchor="middle">endpoints over time →</text>
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
  stroke: var(--ls-line);
  stroke-width: 1.5;
}
.curve {
  fill: none;
  stroke-width: 3;
  stroke-linecap: round;
}
.complexity {
  stroke: var(--ls-orange);
}
.velocity {
  stroke: var(--ls-mint);
}
.cross {
  fill: var(--ls-gold);
  stroke: var(--ls-bg);
  stroke-width: 2;
}
.lbl {
  font-size: 12px;
  font-weight: 800;
}
.complexity-t {
  fill: var(--ls-orange);
}
.velocity-t {
  fill: var(--ls-mint);
}
.cap {
  fill: var(--ls-faint);
  font-size: 11px;
  font-style: italic;
}
</style>
