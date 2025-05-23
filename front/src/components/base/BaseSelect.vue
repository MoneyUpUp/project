<template>
  <div class="base-select-wrapper">
    <select
      :value="modelValue"
      @change="handleChange"
      class="base-select"
    >
      <option
        disabled
        value=""
      >
        {{ placeholder }}
      </option>
      <option
        v-for="option in options"
        :key="option"
        :value="option"
      >
        {{ option }}
      </option>
    </select>
  </div>
</template>

<script setup>
defineProps({
  modelValue: [String, Number],
  options: {
    type: Array,
    required: true,
  },
  placeholder: {
    type: String,
    default: '선택하세요',
  },
})
const emit = defineEmits(['update:modelValue', 'change'])

function handleChange(e) {
  const value = e.target.value
  emit('update:modelValue', value)
  emit('change', value)
}
</script>

<style scoped>
.base-select-wrapper {
  position: relative;
}

.base-select {
  width: 100%;
  padding: 0.625rem 1rem;
  font-size: 0.95rem;
  border-radius: 8px;
  border: 1px solid #ccc;
  background-color: #fff;
  color: #333;
  transition: all 0.2s ease;
  appearance: none;

  background-image: url("data:image/svg+xml,%3Csvg fill='none' height='20' viewBox='0 0 24 24' width='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M7 10l5 5 5-5' stroke='%23999' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 1rem;
  padding-right: 2.5rem;
}

.base-select:focus {
  border-color: #43b883;
  box-shadow: 0 0 0 3px rgba(67, 184, 131, 0.15);
  outline: none;
}

.base-select:hover {
  border-color: #999;
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.05);
}
</style>
