<template>
  <button :class="[
    'button',
    `button--${type}`,
    { 'is-full': fullWidth }
  ]" :disabled="disabled" @click="$emit('click')">
    <slot />
  </button>
</template>

<script setup>
defineProps({
  type: {
    type: String,
    default: 'primary', // primary | outline | ghost
  },
  disabled: Boolean,
  fullWidth: Boolean,
});
</script>

<style scoped>
.button.is-full {
  width: 100%;
}
</style>
