<script setup lang="ts">
// Slide 18: the event loop is one lane — a single blocking call parks
// every request queued behind it. With `fixed`, the blocking work moves
// off to a worker thread and the lane keeps flowing.
defineProps<{ fixed?: boolean }>()
const done = ['req 2', 'req 1']
const waiting = ['req 6', 'req 5', 'req 4']
</script>

<template>
  <div class="loop">
    <div class="lane">
      <div class="flow" aria-hidden="true">→</div>
      <template v-if="!fixed">
        <div v-for="req in waiting" :key="req" class="chip wait">{{ req }}</div>
        <div class="chip block">
          <span class="mono">pd.read_csv(…)</span>
          <span class="block-note">blocking</span>
        </div>
      </template>
      <template v-else>
        <div v-for="req in waiting" :key="req" class="chip done">{{ req }} ✓</div>
      </template>
      <div v-for="req in done" :key="req" class="chip done">{{ req }} ✓</div>
      <div class="flow" aria-hidden="true">→</div>
    </div>
    <div v-if="fixed" class="worker">
      <span class="worker-label">worker thread</span>
      <span class="chip block">
        <span class="mono">pd.read_csv(…)</span>
        <span class="block-note">off the loop</span>
      </span>
    </div>
    <div class="wait-note muted">
      {{
        fixed
          ? 'the loop keeps moving - the blocking work runs off to the side'
          : '…and everyone behind it waits until it finishes'
      }}
    </div>
  </div>
</template>

<style scoped>
.loop {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
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
.worker {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  margin-top: 0.15rem;
}
.worker-label {
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--ls-faint);
  font-weight: 700;
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
