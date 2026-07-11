<script setup lang="ts">
// Slide 2 (right): everything production wires around that same endpoint.
// Compact bricks so the full stack (10 concerns + the handler) fits on screen.
// Pairs with <StackThink />; reveal this on click for the "until it isn't" beat.
const reality = [
  'Auth & guards',
  'Validation / DTOs',
  'Dependency injection',
  'Middleware stack',
  'Serialization',
  'DB sessions & pooling',
  'Pagination & filtering',
  'Error handling',
  'Logging & tracing',
  'Rate limiting',
]
</script>

<template>
  <div class="col">
    <div class="col-head">What production actually needs</div>
    <div class="tower">
      <div v-for="item in reality" :key="item" class="brick">{{ item }}</div>
      <div class="brick gold">GET /orders → 200</div>
    </div>
  </div>
</template>

<style scoped>
.col {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.col-head {
  font-size: 0.8rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--ls-muted);
}
.tower {
  display: flex;
  flex-direction: column;
  gap: 0.18rem;
}
.brick {
  background: var(--ls-bg-2);
  border: 1px solid var(--ls-line);
  border-radius: 9px;
  padding: 0.23rem 0.78rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--ls-text);
}
.brick.gold {
  background: linear-gradient(135deg, var(--ls-gold), #f0a12a);
  border-color: transparent;
  color: #1a1330;
  font-weight: 800;
  font-family: var(--slidev-code-font-family, monospace);
}
</style>
