<template>
  <!-- 🔹 전체 필터 툴바: 좌측 필터 + 우측 정렬 -->
  <div class="filter-toolbar">
    <div class="filter-header">
      <BaseSelect
        v-model="productStore.selectedBank"
        placeholder="은행 명"
        :options="productStore.bankOptions"
        variant="clean"
      />

      <BaseSelect
        v-model="productStore.selectedTypes"
        placeholder="종류"
        :options="[
          { label: '예•적금', value: 'all' },
          { label: '예금', value: 'deposit' },
          { label: '적금', value: 'saving' },
        ]"
        variant="clean"
      />
    </div>

    <!-- 🔹 정렬 컨트롤 (오른쪽 정렬) -->
    <div class="sort-control">
      <BaseSegmentedControl
        v-model="productStore.sortOption"
        :options="[
          { label: '이름순', value: 'name' },
          { label: '최고 이율순', value: 'rate_max' },
          { label: '기본 이율순', value: 'rate_base' },
        ]"
        variant="default"
      />
    </div>
  </div>

  <hr />
</template>

<script setup>
import BaseSelect from '@/components/base/BaseSelect.vue'

import { useProductStore } from '@/stores/productStore'
import { ref } from 'vue'
import BaseSegmentedControl from '../base/BaseSegmentedControl.vue'

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
.filter-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-top: 5%;
  margin-bottom: 1.5rem;
}

.filter-header {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.sort-control {
  display: flex;
  justify-content: flex-end;
}
</style>
