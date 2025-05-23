<template>
  <div class="back">
    <div class="container">
      <!-- <h1>예적금 리스트 페이지</h1> -->

      <div class="product-header">
        <!-- 은행 드롭다운 -->
        <select v-model="selectedBank" class="custom-select">
          <option v-for="bank in banks" :key="bank">{{ bank }}</option>
        </select>

        <!-- 예금/적금 토글 -->
        <div class="toggle-bg">
          <div class="toggle-labels">
            <RouterLink :to="{ path: '/product/deposit', query: { bank: selectedBank, period: selectedIndex } }"
              class="label" :class="{ active: type === 'deposit' }" @click.prevent="setType('deposit')">예금</RouterLink>
            <RouterLink to="/product/saving" class="label" :class="{ active: type === 'saving' }"
              @click.prevent="setType('saving')">적금</RouterLink>
          </div>
          <div class="toggle-circle" :class="type"></div>
        </div>
      </div>
      <hr>
      <!-- 기간 선택 슬라이더 -->
      <div class="slider-container">
        <input type="range" min="0" max="3" step="1" v-model="selectedIndex" class="range-input"
          :style="{ background: getSliderBackground }" />
        <div class="labels">
          <span :class="{ active: selectedIndex === 0 }">전체</span>
          <span :class="{ active: selectedIndex === 1 }">6개월</span>
          <span :class="{ active: selectedIndex === 2 }">12개월</span>
          <span :class="{ active: selectedIndex === 3 }">24개월</span>
        </div>
      </div>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useRoute, useRouter } from 'vue-router'
import { ref, computed } from 'vue'

const route = useRoute()
const router = useRouter()

const selectedBank = ref('우리은행')
const selectedIndex = ref(1) // 기본값: 6개월

const banks = [
  '국민은행', '우리은행', '신한은행', '하나은행', '카카오뱅크', '토스뱅크',
  '기업은행', '농협', '수협', 'SC제일은행', '씨티은행', '부산은행',
  '경남은행', '대구은행', '전북은행', '광주은행', '제주은행', '케이뱅크', '아이엠뱅크'
]


const type = ref(route.path.includes('saving') ? 'saving' : 'deposit')

const setType = (value) => {
  type.value = value;
  router.push({
    path: `/product/${value}`,
    query: {
      bank: selectedBank.value,
      period: selectedIndex.value
    }
  });
};

const getSliderBackground = computed(() => {
  const percent = (selectedIndex.value / 3) * 100
  return `linear-gradient(to right, #43B883 0%, #43B883 ${percent}%, #D9F1E6 ${percent}%, #D9F1E6 100%)`
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
  width: 100%;
  -webkit-appearance: none;
  height: 10px;
  border-radius: 5px;
  background: linear-gradient(to right, #43B883 0%, #43B883 33.3%, #D9F1E6 33.3%, #D9F1E6 100%);
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
  border: 3px solid #43B883;
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
  color: #43B883;
  font-weight: bold;
}

.toggle-bg {
  width: 110px;
  height: 30px;
  background-color: #43B883;
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
  color: #43B883;
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
  color: #43B883;
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