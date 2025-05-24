<template>
  <div class="base-select-wrapper">
    <select
      :value="modelValue"
      @change="handleChange"
      :class="['base-select', `variant--${variant}`]"
    >
      <!-- 안내용 placeholder (선택 불가능) -->
      <option
        disabled
        value=""
      >
        {{ placeholder }}
      </option>

      <!-- 옵션 리스트 -->
      <option
        v-for="option in options"
        :key="getValue(option)"
        :value="getValue(option)"
      >
        {{ getLabel(option) }}
      </option>
    </select>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: [String, Number],
  options: { type: Array, required: true },
  placeholder: { type: String, default: '선택하세요' },
  variant: { type: String, default: 'default' }, // 'default' | 'clean'
  labelKey: { type: String, default: 'label' },
  valueKey: { type: String, default: 'value' },
})

const emit = defineEmits(['update:modelValue', 'change'])

function handleChange(e) {
  const value = e.target.value
  emit('update:modelValue', value)
  emit('change', value)
}

function getValue(option) {
  return typeof option === 'object' ? option[props.valueKey] : option
}

function getLabel(option) {
  return typeof option === 'object' ? option[props.labelKey] : option
}
</script>

<style scoped lang="scss">
.base-select {
  width: 100%;
  font-size: 0.95rem;
  border-radius: 8px;
  transition: all 0.2s ease;
  appearance: none;
  padding-right: 2.5rem;
  background-image: url("data:image/svg+xml,%3Csvg fill='none' height='20' viewBox='0 0 24 24' width='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M7 10l5 5 5-5' stroke='%23999' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 1rem;
}

.variant--default {
  padding: 0.625rem 1rem;
  padding-right: 3rem;
  border: 1px solid #ccc;
  background-color: #fff;
  color: #333;

  &:focus {
    border-color: #43b883;
    box-shadow: 0 0 0 3px rgba(67, 184, 131, 0.15);
    outline: none;
  }

  &:hover {
    border-color: #999;
    box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.05);
  }
}

.variant--clean {
  padding: 8px;
  font-size: 20px;
  font-weight: bold;
  color: #43b883;
  border: none;
  background: transparent;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg fill='%2343B883' height='20' viewBox='0 0 24 24' width='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 1rem;
  padding-right: 2rem;
}
</style>
