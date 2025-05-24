<template>
  <div class="deposit-list">
    <productListItem
      v-for="item in items"
      :key="item.id"
      :item="item"
    />
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import { useRoute } from 'vue-router'
import productListItem from './productListItem.vue'

const route = useRoute()
const props = defineProps({
  items: Array,
})
</script>

<style scoped>
.deposit-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
