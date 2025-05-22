<template>
  <div class="product-header">
    <!-- 은행 드롭다운 -->
    <select v-model="selectedBank">
      <option v-for="bank in banks" :key="bank">{{ bank }}</option>
    </select>

    <!-- 예금/적금 토글 -->
    <div class="toggle-bg">
    <div class="toggle-labels">
      <RouterLink
        to="/product/deposit"
        class="label"
        :class="{ active: type === 'deposit' }"
        @click.prevent="setType('deposit')"
      >예금</RouterLink>
      <RouterLink
        to="/product/saving"
        class="label"
        :class="{ active: type === 'saving' }"
        @click.prevent="setType('saving')"
      >적금</RouterLink>
    </div>
    <div class="toggle-circle" :class="type"></div>
  </div>

    <!-- 기간 선택 슬라이더 -->
    <div class="period-slider">
      <label>기간 선택</label>
      <input type="range" min="0" max="24" v-model="period" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const selectedBank = ref('우리은행')
const period = ref(6)

const banks = [
  '국민은행', '우리은행', '신한은행', '하나은행', '카카오뱅크', '토스뱅크',
  '기업은행', '농협', '수협', 'SC제일은행', '씨티은행', '부산은행',
  '경남은행', '대구은행', '전북은행', '광주은행', '제주은행', '케이뱅크'
]


const type = ref(route.path.includes('saving') ? 'saving' : 'deposit')

const setType = (value) => {
  type.value = value
  router.push(`/product/${value}`)
}
</script>

<style scoped>
.product-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 24px;
}

select {
  padding: 8px;
}

.period-slider {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.toggle-bg {
  width: 120px;
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
</style>