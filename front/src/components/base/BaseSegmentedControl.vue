<template>
  <div class="segmented-control">
    <button
      v-for="option in options"
      :key="option.value"
      :class="['segment', { active: modelValue === option.value }]"
      @click="toggleOption(option.value)"
    >
      {{ option.label }}
    </button>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: String,
    default: '',
  },
  options: {
    type: Array,
    required: true,
  },
})

const emit = defineEmits(['update:modelValue'])

function toggleOption(value) {
  emit('update:modelValue', value)
}
</script>

<style scoped lang="scss">
.segmented-control {
  display: inline-flex;
  background: #f7f7f8;
  padding: 6px;
  border-radius: 12px;
}

.segment {
  flex: 1;
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #999;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.segment.active {
  background: #ffffff;
  color: #111;
  font-weight: 600;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.05);
}
</style>
