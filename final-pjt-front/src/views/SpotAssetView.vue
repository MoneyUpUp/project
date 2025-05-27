<template>
  <div class="container spot-container">
    <div class="spot-header">
      <BaseSelect
        v-model="store.selectedCommodity"
        placeholder="원자재 명"
        :options="store.commodityOptions"
        style="min-width: 220px"
      />

      <div class="date-range">
        <div class="datepicker-button">
          <label>시작일</label>
          <Datepicker v-model="store.startDate" />
        </div>
        <div class="datepicker-button">
          <label>종료일</label>
          <Datepicker v-model="store.endDate" />
        </div>
      </div>
    </div>

    <div class="chart-wrapper">
      <SpotAssetGraph v-if="store.selectedData.length > 0" />
      <p
        v-if="store.selectedData.length === 0"
        class="no-data-message"
      >
        선택된 기간에 대한 데이터가 없습니다.
      </p>
    </div>
  </div>
</template>

<script setup>
import BaseSelect from '@/components/base/BaseSelect.vue'
import SpotAssetGraph from '@/components/spotAsset/SpotAssetGraph.vue'
import { useSpotAssetStore } from '@/stores/spotAssetStore'
import { watchEffect } from 'vue'
import Datepicker from 'vue3-datepicker'

const store = useSpotAssetStore()

watchEffect(() => {
  if (store.selectedCommodity) {
    store.fetchSpotAssetPrices(store.selectedCommodity)
  }
})
</script>

<style scoped lang="scss">
.spot-container {
  // TODO: 디자인 확정 후 box-shadow, border 추가 고려
  padding: 2rem; /* 패딩 증가 */
  width: 100%;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;

  display: flex;
  flex-direction: column;
  gap: 3rem;
}

.spot-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
}

.date-range {
  display: flex;
  gap: 1.2rem;
}

.datepicker-button {
  display: flex;
  flex-direction: column;
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
  gap: 0.4rem;

  input {
    padding: 0.6rem 1rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background-color: #ffffff;
    color: #374151;
    font-weight: 500;
    cursor: pointer;
    font-size: 15px;
    transition:
      background-color 0.2s ease,
      border-color 0.2s ease,
      box-shadow 0.2s ease;

    &:hover {
      background-color: #f0f0f0;
      border-color: #9ca3af;
    }

    &:focus {
      border-color: #4f46e5;
      outline: none;
      background-color: #fff;
      box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
    }
  }
}

.chart-wrapper {
  padding-top: 2.5rem;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .spot-container {
    padding: 1rem;
    margin-top: 2rem;
  }
  .spot-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .date-range {
    width: 100%;
    flex-direction: column;
    gap: 0.8rem;
  }

  .datepicker-button {
    width: 100%;
  }
}
</style>
