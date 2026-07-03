<script setup lang="ts">
// Slide 17: the event loop is one lane — a single blocking call parks
// every request queued behind it.
const done = ['req 1', 'req 2']
const waiting = ['req 4', 'req 5', 'req 6']
</script>

<template>
  <div class="loop">
    <div class="lane-label">the event loop — one lane, shared by every request</div>
    <div class="lane">
      <div class="flow" aria-hidden="true">→</div>
      <div v-for="req in waiting" :key="req" class="chip wait">{{ req }}</div>
      <div class="chip block">
        <span class="mono">time.sleep(2)</span>
        <span class="block-note">blocking</span>
      </div>
      <div v-for="req in done" :key="req" class="chip done">{{ req }} ✓</div>
      <div class="flow" aria-hidden="true">→</div>
    </div>
    <div class="wait-note muted">…and everyone behind it waits the full 2&nbsp;s</div>
  </div>
</template>

<style scoped>
.loop {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}
.lane-label {
  font-size: 0.7rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: 800;
  color: var(--ls-faint);
  text-align: center;
}
.lane {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  background: var(--ls-bg-2);
  border: 1px solid var(--ls-line);
  border-radius: 999px;
  padding: 0.5rem 1rem;
}
.chip {
  border-radius: 999px;
  padding: 0.3rem 0.7rem;
  font-size: 0.78rem;
  font-weight: 700;
  white-space: nowrap;
}
.chip.done {
  color: var(--ls-mint);
  border: 1px solid var(--ls-mint);
}
.chip.wait {
  color: var(--ls-faint);
  border: 1px dashed var(--ls-faint);
}
.chip.block {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--ls-cream);
  background: rgba(242, 107, 33, 0.18);
  border: 1.5px solid var(--ls-orange);
  padding: 0.35rem 0.9rem;
}
.chip.block .mono {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
}
.chip.block .block-note {
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--ls-orange);
}
.flow {
  color: var(--ls-faint);
  font-size: 1.1rem;
  font-weight: 700;
}
.wait-note {
  font-size: 0.78rem;
  font-style: italic;
  text-align: center;
}
</style>
