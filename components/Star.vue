<script setup lang="ts">
// The five-point star motif. Defaults to the theme gold; pass `color`/`size`.
withDefaults(defineProps<{ size?: number | string; color?: string; glow?: boolean }>(), {
  size: 24,
  glow: false,
})
</script>

<template>
  <svg
    class="ls-star"
    :class="{ glow }"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    :style="{ color: color ?? 'var(--ls-gold)' }"
    aria-hidden="true"
  >
    <path
      fill="currentColor"
      d="M12 2 L14.35 8.76 L21.51 8.91 L15.80 13.24 L17.88 20.09 L12 16 L6.12 20.09 L8.20 13.24 L2.49 8.91 L9.65 8.76 Z"
    />
  </svg>
</template>

<style scoped>
.ls-star {
  display: inline-block;
  vertical-align: middle;
}
.ls-star.glow {
  filter: drop-shadow(0 0 6px rgba(244, 178, 62, 0.6));
}
</style>
