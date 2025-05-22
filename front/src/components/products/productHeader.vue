<template>
  <div class="product-header">
    <!-- 은행 드롭다운 -->
    <select v-model="selectedBank">
      <option v-for="bank in banks" :key="bank">{{ bank }}</option>
    </select>

    <!-- 예금/적금 토글 -->
    <div class="product-toggle">
      <RouterLink
        to="/product/deposit"
        :class="{ active: type === '예금' }"
      >
        예금
      </RouterLink>
      <RouterLink
        to="/product/saving"
        :class="{ active: type === '적금' }"
      >
        적금
      </RouterLink>
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
const type = ref(route.path.includes('saving') ? '적금' : '예금')

const selectedBank = ref('우리은행')
const period = ref(6)

const banks = [
  '국민은행', '우리은행', '신한은행', '하나은행', '카카오뱅크', '토스뱅크',
  '기업은행', '농협', '수협', 'SC제일은행', '씨티은행', '부산은행',
  '경남은행', '대구은행', '전북은행', '광주은행', '제주은행', '케이뱅크'
]
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

.product-toggle a {
  padding: 6px 12px;
  border-radius: 20px;
  background: #eee;
  margin-left: 4px;
  text-decoration: none;
  color: #222;
}

.product-toggle .active {
  background-color: #43B883;
  color: white;
}

.period-slider {
  flex: 1;
  display: flex;
  flex-direction: column;
}
</style>