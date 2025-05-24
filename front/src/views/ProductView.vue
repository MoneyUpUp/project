<template>
  <div class="back">
    <div class="container">
      <!-- ✅ 은행 선택 드롭다운 -->
      <div class="product-header">
        <BaseSelect
          v-model="productStore.selectedBank"
          placeholder="은행 명"
          :options="productStore.bankOptions"
          variant="clean"
        />

        <!-- ✅ 예금/적금 토글 버튼 -->
        <BaseSegmentedControl
          v-model="productStore.selectedTypes"
          :options="[
            { label: '예금', value: 'deposit' },
            { label: '적금', value: 'saving' },
          ]"
        />
      </div>

      <hr />

      <!-- ✅ 기간 슬라이더 -->
      <div class="slider-container">
        <input
          type="range"
          min="0"
          max="3"
          step="1"
          v-model="productStore.selectedIndex"
          class="range-input"
          :style="{ background: getSliderBackground }"
        />
        <div class="labels">
          <span :class="{ active: productStore.selectedIndex === 0 }">전체</span>
          <span :class="{ active: productStore.selectedIndex === 1 }">6개월</span>
          <span :class="{ active: productStore.selectedIndex === 2 }">12개월</span>
          <span :class="{ active: productStore.selectedIndex === 3 }">24개월</span>
        </div>
      </div>

      <!-- ✅ 리스트 출력 -->
      <ProductList :items="productStore.filteredItems" />

      <RouterView />
    </div>
  </div>
</template>
<script setup>
// ✅ 필요한 모듈 불러오기
import BaseSegmentedControl from '@/components/base/BaseSegmentedControl.vue'
import BaseSelect from '@/components/base/BaseSelect.vue'
import ProductList from '@/components/product/ProductList.vue'
import { useProductStore } from '@/stores/productStore'
import { computed, onMounted } from 'vue'
import { RouterView, useRoute, useRouter } from 'vue-router'

// ✅ 상태 저장소 가져오기
const productStore = useProductStore()
const route = useRoute()
const router = useRouter()

// ✅ 예금/적금 탭 전환 핸들러
const setType = (value) => {
  productStore.type = value
  router.push({
    path: `/product/${value}`,
    query: {
      bank: productStore.selectedBank,
      period: productStore.selectedIndex,
    },
  })
}

// ✅ 슬라이더 스타일 계산
const getSliderBackground = computed(() => {
  const percent = (productStore.selectedIndex / 3) * 100
  return `linear-gradient(to right, #43B883 0%, #43B883 ${percent}%, #D9F1E6 ${percent}%, #D9F1E6 100%)`
})

// ✅ 최초 데이터 패치
onMounted(() => {
  productStore.fetchAllProducts()
})
</script>

<style scoped>
.product-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 5%;
  margin-bottom: 24px;
}

select {
  padding: 8px;
}

.slider-container {
  width: 955px;
  margin: 50px auto;
}

.range-input {
  -webkit-appearance: none;
  width: 100%;
  height: 10px;
  border-radius: 5px;
  background: linear-gradient(to right, #43b883 0%, #43b883 33.3%, #d9f1e6 33.3%, #d9f1e6 100%);
  outline: none;
  transition: background 0.3s;
}

.range-input::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: white;
  border: 3px solid #43b883;
  cursor: pointer;
  margin-top: -4px;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.2);
}

.labels {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.labels span {
  font-size: 14px;
  color: #999;
}

.labels .active {
  color: #43b883;
  font-weight: bold;
}

.toggle-bg {
  width: 110px;
  height: 30px;
  background-color: #43b883;
  border-radius: 15px;
  position: relative;
  display: flex;
  align-items: center;
  padding: 0 6px;
  box-sizing: border-box;
}

.toggle-labels {
  width: 100%;
  display: flex;
  justify-content: space-between;
  z-index: 1;
  position: relative;
}

.label {
  font-size: 13px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.44);
  text-decoration: none;
  padding: 2px 10px;
  border-radius: 11px;
}

.label.active {
  color: #43b883;
  background-color: white;
}

.toggle-circle {
  width: 45px;
  height: 22px;
  background-color: white;
  border-radius: 11px;
  position: absolute;
  top: 4px;
  left: 6px;
  transition: left 0.3s;
  z-index: 0;
}

.toggle-circle.saving {
  left: 69px;
}

.custom-select {
  font-size: 20px;
  font-weight: bold;
  color: #43b883;
  border: none;
  background: transparent;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-image: url('data:image/svg+xml;utf8,<svg fill="green" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>');
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  padding-right: 2rem;
}
</style>
