<script setup lang="ts">
// Slide 13: the request pipeline, in the order it actually runs.
const stages = [
  { label: 'Request', kind: 'io' },
  { label: 'Middleware', kind: 'mw', note: 'app · router scope' },
  { label: 'Guards', kind: 'guard', note: 'authorize / reject' },
  { label: 'Handler', kind: 'handler', note: 'your code' },
  { label: 'Response', kind: 'io' },
]
</script>

<template>
  <div class="chain">
    <template v-for="(stage, i) in stages" :key="stage.label">
      <div class="node" :class="stage.kind">
        <div class="node-label">{{ stage.label }}</div>
        <div v-if="stage.note" class="node-note">{{ stage.note }}</div>
      </div>
      <div v-if="i < stages.length - 1" class="link" aria-hidden="true">›</div>
    </template>
  </div>
</template>

<style scoped>
.chain {
  display: flex;
  align-items: stretch;
  justify-content: center;
  gap: 0.25rem;
  flex-wrap: nowrap;
}
.node {
  flex: 1 1 0;
  min-width: 0;
  background: var(--ls-bg-2);
  border: 1px solid var(--ls-line);
  border-radius: 12px;
  padding: 0.7rem 0.6rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.2rem;
}
.node-label {
  font-weight: 800;
  font-size: 0.95rem;
  color: var(--ls-text);
}
.node-note {
  font-size: 0.68rem;
  color: var(--ls-muted);
  font-style: italic;
}
/* request / response endpoints */
.node.io {
  background: transparent;
  border-style: dashed;
  border-color: var(--ls-faint);
}
.node.io .node-label {
  color: var(--ls-faint);
}
.node.mw {
  border-left: 3px solid var(--ls-violet);
}
.node.guard {
  border-left: 3px solid var(--ls-mint);
}
.node.handler {
  border-left: 3px solid var(--ls-gold);
}
.link {
  align-self: center;
  color: var(--ls-faint);
  font-size: 1.5rem;
  font-weight: 700;
  padding: 0 0.1rem;
}
</style>
