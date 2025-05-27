<template>
  <div class="range-slider">
    <input
      type="range"
      min="0"
      max="3"
      step="1"
      :value="modelValue"
      @input="onInput"
      class="range-input"
      :style="{ background: sliderBackground }"
    />
    <div class="labels">
      <span :class="{ active: modelValue === 0 }">전체</span>
      <span :class="{ active: modelValue === 1 }">6개월</span>
      <span :class="{ active: modelValue === 2 }">12개월</span>
      <span :class="{ active: modelValue === 3 }">24개월</span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: { type: Number, required: true },
})

const emit = defineEmits(['update:modelValue'])

function onInput(e) {
  emit('update:modelValue', parseInt(e.target.value))
}

const sliderBackground = computed(() => {
  const percent = (props.modelValue / 3) * 100
  return `linear-gradient(to right, #43b883 0%, #43b883 ${percent}%, #d9f1e6 ${percent}%, #d9f1e6 100%)`
})
</script>

<style scoped lang="scss">
.range-slider {
  width: 100%;
  max-width: 955px;
  margin: 40px auto;
}

.range-input {
  -webkit-appearance: none;
  width: 100%;
  height: 10px;
  border-radius: 5px;
  background: #d9f1e6;
  outline: none;
  transition: background 0.3s;
}

.range-input::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: white;
  border: 3px solid #43b883;
  cursor: pointer;
  margin-top: -4px;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.2);
}

.labels {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.labels span {
  font-size: 14px;
  color: #999;
}

.labels .active {
  color: #43b883;
  font-weight: bold;
}
</style>
