<script setup lang="ts">
// Slide 12: configuration set high in the tree, overridden where it matters.
// app → router / controller → handler, each layer narrowing the scope.
// Router and controller sit at the same layer (same override precedence).
const layers = [
  { name: 'App', sets: 'defaults: deps, guards, middleware, response', tone: 'app' },
  {
    name: 'Router / Controller',
    sets: 'override: prefix & resource guards, deps, DTOs',
    tone: 'router',
  },
  { name: 'Handler', sets: 'final say: per-route config wins', tone: 'handler' },
]
</script>

<template>
  <div class="layers">
    <div
      v-for="(layer, i) in layers"
      :key="layer.name"
      class="layer"
      :class="layer.tone"
      :style="{ marginLeft: `${i * 2.2}rem` }"
    >
      <div class="layer-name">{{ layer.name }}</div>
      <div class="layer-sets">{{ layer.sets }}</div>
      <div v-if="i < layers.length - 1" class="cascade" aria-hidden="true">↳</div>
    </div>
  </div>
</template>

<style scoped>
.layers {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  max-width: 46rem;
}
.layer {
  position: relative;
  background: var(--ls-bg-2);
  border: 1px solid var(--ls-line);
  border-left: 4px solid var(--ls-faint);
  border-radius: 12px;
  padding: 0.6rem 1rem;
}
.layer-name {
  font-weight: 800;
  font-size: 1rem;
  color: var(--ls-text);
}
.layer-sets {
  font-size: 0.82rem;
  color: var(--ls-muted);
  margin-top: 0.1rem;
}
.cascade {
  position: absolute;
  left: 0.7rem;
  bottom: -0.62rem;
  color: var(--ls-faint);
  font-size: 1rem;
  z-index: 2;
}
.layer.app {
  border-left-color: var(--ls-violet);
}
.layer.router {
  border-left-color: var(--ls-blue);
}
.layer.handler {
  border-left-color: var(--ls-gold);
}
.layer.handler .layer-name {
  color: var(--ls-gold);
}
</style>
