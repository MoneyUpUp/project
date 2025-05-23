<template>
  <component
    :is="isRouter ? 'RouterLink' : 'button'"
    :to="isRouter ? to : undefined"
    :class="['button', `button--${type}`, { 'is-full': fullWidth }]"
    :disabled="disabled"
    @click="$emit('click')"
  >
    <slot />
  </component>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps({
  to: String,
  type: {
    type: String,
    default: 'primary',
  },
  disabled: Boolean,
  fullWidth: Boolean,
})

const isRouter = computed(() => !!props.to)
</script>

<style scoped>
.button {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.button--primary {
  background-color: #43b883;
  color: white;
  border: none;
}

.button--primary:hover {
  background-color: #369f6d;
}

.button--secondary {
  background-color: white;
  color: #43b883;
  border: 1px solid #43b883;
}

.button--secondary:hover {
  background-color: #f0fef7;
}

.button.is-full {
  width: 100%;
}
</style>
