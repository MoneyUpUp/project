<template>
  <div class="advanced-filter">
    <h4 class="title">고급 필터</h4>

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

    <div class="filter-section">
      <h5 class="subtitle">우대 조건</h5>
      <div class="filter-group">
        <BaseCheckbox
          v-model="filters.specialRate"
          label="우대금리 제공"
        >
          우대금리 제공
        </BaseCheckbox>
      </div>
    </div>

    <div class="filter-section">
      <h5 class="subtitle">가입 제한</h5>
      <div class="filter-group">
        <BaseCheckbox
          v-model="filters.noRestriction"
          label="제한 없음"
        >
          제한 없음
        </BaseCheckbox>
        <BaseCheckbox
          v-model="filters.individualOnly"
          label="실명의 개인 전용"
        >
          실명의 개인 전용
        </BaseCheckbox>
      </div>
    </div>

    <div class="filter-section">
      <h5 class="subtitle">기타 조건</h5>
      <div class="filter-group">
        <BaseCheckbox
          v-model="filters.hasMinAmount"
          label="최소 가입금액 존재"
        >
          최소 가입금액 존재
        </BaseCheckbox>
        <BaseCheckbox
          v-model="filters.customTerm"
          label="가입 기간 자유 선택 가능"
        >
          가입 기간 자유 선택 가능
        </BaseCheckbox>
        <BaseCheckbox
          v-model="filters.hasMaturityRate"
          label="만기 이율 조건 있음"
        >
          만기 이율 조건 있음
        </BaseCheckbox>
      </div>
    </div>
  </div>
</template>

<script setup>
import BaseCheckbox from '@/components/base/BaseCheckbox.vue'
import { reactive, watch } from 'vue'

const filters = reactive({
  internet: false,
  smartphone: false,
  telephone: false,
  branch: false,
  specialRate: false,
  noRestriction: false,
  individualOnly: false,
  hasMinAmount: false,
  customTerm: false,
  hasMaturityRate: false,
})

watch(filters, (newFilters) => {
  console.log('적용된 고급 필터:', newFilters)
})
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
</style>
