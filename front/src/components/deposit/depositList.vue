<template>
  <div class="deposit-list">
    <depositListItem v-for="n in 10" :key="n" />
  </div>
</template>

<script setup>
import depositListItem from './depositListItem.vue'
</script>

<style scoped>
.deposit-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
