<template>
  <label class="base-checkbox">
    <input
      type="checkbox"
      :checked="modelValue"
      @change="$emit('update:modelValue', $event.target.checked)"
    />
    <span class="checkbox-custom"></span>
    <span class="checkbox-label"><slot /></span>
  </label>
</template>

<script setup>
defineProps({
  modelValue: Boolean,
})

defineEmits(['update:modelValue'])
</script>

<style scoped lang="scss">
.base-checkbox {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  user-select: none;
  font-size: 14px;
}

.base-checkbox input {
  display: none;
}

.checkbox-custom {
  width: 16px;
  height: 16px;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
  position: relative;
}

.base-checkbox input:checked + .checkbox-custom {
  background-color: #43b883;
  border-color: #43b883;
}

.base-checkbox input:checked + .checkbox-custom::after {
  content: '';
  position: absolute;
  left: 4px;
  top: 0px;
  width: 4px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}
</style>
