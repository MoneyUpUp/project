<template>
  <div class="advanced-filter">
    <h4 class="title">고급 필터</h4>

    <div class="filter-section">
      <h5 class="subtitle">가입 기간</h5>
      <div class="range-wrapper">
        <input
          type="range"
          min="0"
          max="3"
          step="1"
          v-model="selectedTerm"
          class="range-input"
          :style="rangeBackground"
        />
        <div class="range-labels">
          <span :class="labelClasses(0)">6개월</span>
          <span :class="labelClasses(1)">12개월</span>
          <span :class="labelClasses(2)">24개월</span>
          <span :class="labelClasses(3)">36개월</span>
        </div>
      </div>
    </div>
    <div class="filter-section">
      <h5 class="subtitle">가입 방법</h5>
      <div class="filter-group">
        <BaseCheckbox
          v-model="filters.internet"
          label="인터넷"
        >
          인터넷
        </BaseCheckbox>
        <BaseCheckbox
          v-model="filters.smartphone"
          label="스마트폰"
        >
          스마트폰
        </BaseCheckbox>
        <BaseCheckbox
          v-model="filters.telephone"
          label="전화"
        >
          전화
        </BaseCheckbox>
        <BaseCheckbox
          v-model="filters.branch"
          label="영업점"
        >
          영업점
        </BaseCheckbox>
      </div>
    </div>
  </div>
</template>

<script setup>
import BaseCheckbox from '@/components/base/BaseCheckbox.vue'
import { useProductStore } from '@/stores/productStore'
import { computed } from 'vue'

const productStore = useProductStore()

const selectedTerm = computed({
  get: () => {
    const termMap = [6, 12, 24, 36]
    return termMap.indexOf(productStore.selectedTerm ?? 6)
  },
  set: (val) => {
    const termMap = [6, 12, 24, 36]
    productStore.selectedTerm = termMap[val]
  },
})

const filters = computed(() => productStore.advancedFilters)

const rangeBackground = computed(() => {
  const percent = (selectedTerm.value / 3) * 100
  return {
    background: `linear-gradient(to right, #43b883 0%, #43b883 ${percent}%, #ddd ${percent}%, #ddd 100%)`,
  }
})

const labelClasses = (index) => {
  return {
    active: selectedTerm.value === index,
    filled: index >= 0 && index <= selectedTerm.value,
  }
}
</script>

<style scoped lang="scss">
.advanced-filter {
  width: 220px;
  background-color: #fff;
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 16px;
  font-family: sans-serif;

  .title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 12px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 6px;
  }

  .filter-section {
    margin-bottom: 20px;

    .subtitle {
      font-size: 15px;
      font-weight: 600;
      color: #333;
      margin-bottom: 8px;
    }

    .filter-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
  }
}

.range-wrapper {
  display: flex;
  flex-direction: column;
  gap: 8px;

  .range-input {
    width: 100%;
    appearance: none;
    height: 8px;
    border-radius: 4px;
    outline: none;

    &::-webkit-slider-thumb {
      appearance: none;
      width: 16px;
      height: 16px;
      background: #43b883;
      border-radius: 50%;
      cursor: pointer;
    }
  }

  .range-labels {
    display: flex;
    justify-content: space-between;
    font-size: 13px;

    span {
      color: #aaa;
      font-weight: normal;
    }

    span.active,
    span.filled {
      color: #43b883;
      font-weight: bold;
    }
  }
}

.horizontal-scroll {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 4px 0;

  .term-button {
    white-space: nowrap;
    padding: 6px 12px;
    border: 1px solid #ddd;
    border-radius: 6px;
    background: #f7f7f7;
    font-size: 14px;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #e0f4ec;
    }
  }
}
</style>
