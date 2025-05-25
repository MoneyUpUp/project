<template>
  <!-- 🔹 필터 헤더: 은행 + 예/적금 + 고급필터 -->
  <div class="filter-header">
    <BaseSelect
      v-model="productStore.selectedBank"
      placeholder="은행 명"
      :options="productStore.bankOptions"
      variant="clean"
    />

    <BaseSegmentedControl
      v-model="productStore.selectedTypes"
      :options="[
        { label: '예금', value: 'deposit' },
        { label: '적금', value: 'saving' },
      ]"
    />
  </div>

  <!-- 🔹 정렬 컨트롤 (리스트 위쪽에 위치) -->
  <div class="sort-control">
    <BaseSelect
      v-model="productStore.sortOption"
      placeholder="정렬 기준"
      :options="[
        { label: '이름순', value: 'name' },
        { label: '금리순', value: 'rate' },
        { label: '최신순', value: 'latest' },
        { label: '기간순', value: 'term' },
        { label: '은행순', value: 'bank' },
      ]"
      variant="default"
    />
  </div>

  <hr />
</template>

<script setup>
import BaseSegmentedControl from '@/components/base/BaseSegmentedControl.vue'
import BaseSelect from '@/components/base/BaseSelect.vue'

import { useProductStore } from '@/stores/productStore'
import { ref } from 'vue'

const productStore = useProductStore()

const showAdvanced = ref(false)
const sortOrder = ref('default')
const filters = ref({
  onlyOnline: false,
  onlyCompound: false,
  onlyPreferential: false,
})

function resetFilters() {
  productStore.selectedBank = 'all'
  productStore.selectedTypes = ['deposit', 'saving']
  sortOrder.value = 'default'
  filters.value = {
    onlyOnline: false,
    onlyCompound: false,
    onlyPreferential: false,
  }
}

function applyFilters() {
  // TODO: 정렬 및 고급 필터 로직 처리
  console.log('정렬:', sortOrder.value, '필터:', filters.value)
}
</script>

<style scoped lang="scss">
.filter-header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  margin-top: 5%;
  margin-bottom: 1.5rem;
  gap: 1.5rem;
  flex-direction: row;
}

.sort-control {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
}
</style>
