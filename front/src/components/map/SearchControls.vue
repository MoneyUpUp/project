<template>
  <div class="search-controls-container">
    <BaseSelect
      v-model="mapStore.selectedState"
      :options="mapStore.states"
      placeholder="도/시"
      @change="mapStore.onStateChange"
      variant="default"
    />

    <BaseSelect
      v-model="mapStore.selectedCity"
      :options="mapStore.cities"
      placeholder="시/군/구"
      variant="default"
    />

    <BaseSelect
      v-model="mapStore.selectedBank"
      :options="mapStore.banks"
      placeholder="은행"
      variant="default"
    />

    <BaseButton @click="mapStore.onSearch" class="search-button">검색</BaseButton>
  </div>
</template>

<script setup>
import BaseButton from '@/components/base/BaseButton.vue'
import BaseSelect from '@/components/base/BaseSelect.vue'

import { useMapStore } from '@/stores/mapStore.js'

const mapStore = useMapStore()
</script>

<style scoped>
.search-controls-container {
  display: flex;
  flex-direction: column; /* 요소들이 세로로 정렬되도록 */
  gap: 1rem; /* 요소들 사이의 간격 */
  align-items: stretch; /* 자식 요소들이 컨테이너 너비를 채우도록 */
}

.search-controls-container > * {
  width: 100%; /* 모든 자식 요소가 너비를 가득 채우도록 */
}

.search-button {
  /* margin-left: auto; 제거 */
}
</style>
