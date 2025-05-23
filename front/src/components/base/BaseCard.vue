<template>
  <div class="base-card">
    <slot />
  </div>
</template>

<script setup>
// 나중에 props로 hover/shadow/tight 등 옵션도 받을 수 있음
</script>

<style scoped>
.base-card {
  background-color: white;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
}
.base-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
</style>
