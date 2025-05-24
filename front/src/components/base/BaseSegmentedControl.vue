<template>
  <div class="segmented-control">
    <button
      v-for="option in options"
      :key="option.value"
      :class="['segment', { active: modelValue.includes(option.value) }]"
      @click="toggleOption(option.value)"
    >
      <span
        v-if="modelValue.includes(option.value)"
        class="check"
        >✔</span
      >
      {{ option.label }}
    </button>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: Array,
    default: () => [],
  },
  options: {
    type: Array,
    required: true, // [{ label: '예금', value: 'deposit' }, { label: '적금', value: 'saving' }]
  },
})

const emit = defineEmits(['update:modelValue'])

function toggleOption(value) {
  const newValue = [...props.modelValue]
  const index = newValue.indexOf(value)

  if (index >= 0) {
    newValue.splice(index, 1) // 이미 선택된 값이면 제거
  } else {
    newValue.push(value) // 선택되지 않은 값이면 추가
  }

  emit('update:modelValue', newValue)
}
</script>

<style scoped lang="scss">
.segmented-control {
  display: flex;
  gap: 0.5rem;
}

.segment {
  padding: 0.6rem 1.2rem;
  border-radius: 999px;
  border: 2px solid #ccc;
  background: #fff;
  color: #222;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.segment.active {
  border-color: #2eb474;
  color: #2eb474;
}

.check {
  font-size: 0.9rem;
  color: #2eb474;
}
</style>
