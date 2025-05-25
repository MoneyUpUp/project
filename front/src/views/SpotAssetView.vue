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
          <label for="startday">시작일</label>
          <Datepicker v-model="store.startDate" />
        </div>
        <div class="datepicker-button">
          <label for="endday">종료일</label>
          <Datepicker v-model="store.endDate" />
        </div>
      </div>
    </div>

    <div class="chart-wrapper">
      <silverGraph
        :commodity="store.selectedCommodity"
        :start-date="store.startDate"
        :end-date="store.endDate"
      />
    </div>
  </div>
</template>

<script setup>
import BaseSelect from '@/components/base/BaseSelect.vue'
import silverGraph from '@/components/silver/silverGraph.vue'
import Datepicker from 'vue3-datepicker'
import { useSpotAssetStore } from '@/stores/spotAssetStore'

const store = useSpotAssetStore()
</script>

<style scoped lang="scss">
.spot-container {
  margin-top: 5rem;
  width: 100%;

  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.spot-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.date-range {
  display: flex;
  gap: 1rem;
}

.datepicker-button {
  display: flex;
  flex-direction: column;
  font-size: 0.875rem;
  font-weight: 600;
  color: #1f2937;
  gap: 0.3rem;

  input {
    padding: 0.5rem 0.75rem;
    border: 1px solid #3b82f6;
    border-radius: 6px;
    background-color: #e0f2ff;
    color: #1e3a8a;
    font-weight: 500;
    cursor: pointer;
    font-size: 14px;
    transition:
      background-color 0.2s,
      border-color 0.2s;

    &:hover {
      background-color: #dbeafe;
    }

    &:focus {
      border-color: #2563eb;
      outline: none;
      background-color: #fff;
      box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.3);
    }
  }
}

.chart-wrapper {
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}
</style>
