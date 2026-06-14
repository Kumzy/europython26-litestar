<script setup lang="ts">
// Slide 2 (left): the endpoint we think we're shipping — one handler, zero
// ceremony. Pairs with <StackReality />, revealed on click.
</script>

<template>
  <div class="col">
    <div class="col-head">What we think we build</div>
    <div class="tower">
      <div class="brick gold">GET /orders → 200</div>
    </div>
    <div class="col-foot">one handler, zero ceremony</div>
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
  gap: 0.28rem;
}
.brick {
  background: var(--ls-bg-2);
  border: 1px solid var(--ls-line);
  border-radius: 9px;
  padding: 0.32rem 0.78rem;
  font-size: 0.82rem;
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
.col-foot {
  font-size: 0.78rem;
  font-style: italic;
  color: var(--ls-faint);
  margin-top: 0.2rem;
}
</style>
