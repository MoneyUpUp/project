<template>
  <div class="deposit-list">
    <productListItem
      v-for="item in sortedItems"
      :key="item.id"
      :item="item"
    />
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/productStore'
import { computed, defineProps } from 'vue'
import { useRoute } from 'vue-router'
import productListItem from './productListItem.vue'

const route = useRoute()
const props = defineProps({
  items: Array,
})

const productStore = useProductStore()

const sortedItems = computed(() => {
  if (productStore.sortOption === 'rate') {
    return [...props.items].sort((a, b) => {
      const maxRateA = Math.max(...a.options.map((opt) => parseFloat(opt.intr_rate2 || 0)))
      const maxRateB = Math.max(...b.options.map((opt) => parseFloat(opt.intr_rate2 || 0)))
      return maxRateB - maxRateA
    })
  } else if (productStore.sortOption === 'latest') {
    return [...props.items].sort((a, b) => new Date(b.dcls_strt_day) - new Date(a.dcls_strt_day))
  }
  return props.items
})
</script>

<style scoped>
.deposit-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-right: 4px; /* Optional for scrollbar spacing */
}
</style>
