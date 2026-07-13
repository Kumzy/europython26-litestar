<script setup lang="ts">
// Slide 14: port of the layered-config flow built for the litestar v2 website
// (litestar-vue-flow / LitestarWorkflow.vue), restyled for Stellar Drift.
// Nested boxes: Application layer → Router/Controller layer → two Handler
// layers, with config pills chained by animated dashed connectors.
</script>

<template>
  <div class="flow">
    <div class="box app">
      <div class="box-label violet">Application layer</div>
      <div class="pill app-pill">Application configuration</div>
      <div class="box router">
        <span class="inlet">
          <span class="vline grow" />
          <span class="arrow">▾</span>
        </span>
        <div class="box-label blue">Router / Controller layer</div>
        <div class="pill router-pill">Router / Controller configuration</div>
        <div class="connector">
          <span class="vline" />
        </div>
        <div class="split">
          <span class="hline" />
          <span class="drop left"><span class="vline" /><span class="arrow">▾</span></span>
          <span class="drop right"><span class="vline" /><span class="arrow">▾</span></span>
        </div>
        <div class="handlers">
          <div class="box handler">
            <div class="box-label gold">Handler layer</div>
            <div class="pill handler-pill">GET /users</div>
          </div>
          <div class="box handler">
            <div class="box-label gold">Handler layer</div>
            <div class="pill handler-pill">POST /users</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.flow {
  max-width: 44rem;
}
.pill,
.box-label {
  white-space: nowrap;
}
.box {
  border: 1px solid var(--ls-line);
  border-radius: 12px;
  padding: 0.4rem 0.8rem 0.55rem;
}
.box.app {
  background: color-mix(in srgb, var(--ls-violet) 6%, transparent);
}
.box.router {
  background: color-mix(in srgb, var(--ls-blue) 7%, transparent);
  position: relative;
  margin-top: 1rem;
}
.inlet {
  position: absolute;
  top: -1rem;
  left: 50%;
  transform: translateX(-50%);
  height: 2.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.inlet .vline.grow {
  flex: 1;
  height: auto;
}
.box.handler {
  background: color-mix(in srgb, var(--ls-gold) 7%, transparent);
  flex: 1;
}
.box-label {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 0.25rem;
}
.box-label.violet {
  color: var(--ls-violet);
}
.box-label.blue {
  color: var(--ls-blue);
}
.box-label.gold {
  color: var(--ls-gold);
}
.pill {
  margin: 0 auto;
  width: fit-content;
  background: var(--ls-bg-2);
  border: 1px solid var(--ls-line);
  border-radius: 8px;
  padding: 0.28rem 1rem;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--ls-text);
}
.app-pill {
  border-color: color-mix(in srgb, var(--ls-violet) 55%, transparent);
}
.router-pill {
  border-color: color-mix(in srgb, var(--ls-blue) 55%, transparent);
}
.handler-pill {
  border-color: color-mix(in srgb, var(--ls-gold) 55%, transparent);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
}
.connector {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0.1rem 0;
}
.vline {
  width: 2px;
  height: 8px;
  background: repeating-linear-gradient(to bottom, var(--ls-faint) 0 4px, transparent 4px 8px);
  animation: dashdown 0.8s linear infinite;
}
.hline {
  position: absolute;
  top: 0;
  left: 25%;
  right: 25%;
  height: 2px;
  background: repeating-linear-gradient(to right, var(--ls-faint) 0 4px, transparent 4px 8px);
  animation: dashright 0.8s linear infinite;
}
.arrow {
  color: var(--ls-faint);
  font-size: 0.6rem;
  line-height: 0.5;
}
/* in PDF export (html.print, set in setup/main.ts) swap the animated gradient
   dashes for real dashed borders — each repeating-linear-gradient otherwise
   becomes a full-canvas tiling pattern that Acrobat composites slowly */
html.print .vline {
  background: none;
  width: 0;
  border-left: 2px dashed var(--ls-faint);
  animation: none;
}
html.print .hline {
  background: none;
  height: 0;
  border-top: 2px dashed var(--ls-faint);
  animation: none;
}
.split {
  position: relative;
  height: 16px;
}
.drop {
  position: absolute;
  top: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.drop.left {
  left: 25%;
  transform: translateX(-50%);
}
.drop.right {
  right: 25%;
  transform: translateX(50%);
}
.handlers {
  display: flex;
  gap: 0.9rem;
}
@keyframes dashdown {
  to {
    background-position-y: 8px;
  }
}
@keyframes dashright {
  to {
    background-position-x: 8px;
  }
}
</style>
