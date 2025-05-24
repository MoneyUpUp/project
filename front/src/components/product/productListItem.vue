<template>
  <BaseCard>
    <div class="item">
      <div class="left">
        <img
          :src="item.bank.logo"
          :alt="item.bank.kor_co_nm"
          @error="onImgError"
        />
        <div class="info">
          <h4>{{ item.fin_prdt_nm }}</h4>
          <p>{{ item.bank.kor_co_rm }} · {{ item.join_member }}</p>
          <span class="tag">방문없이가입</span>
        </div>
      </div>
      <div class="right">
        <p class="rate">
          최고 <strong>{{ maxRate }}</strong>
        </p>
        <p class="base">기본 {{ baseRate }}</p>
      </div>
    </div>
  </BaseCard>
</template>

<script setup>
import BaseCard from '@/components/base/BaseCard.vue'
import { computed } from 'vue'

const props = defineProps({
  item: Object,
})
const baseRate = computed(() => {
  return parseFloat(props.item.options?.[0]?.intr_rate || 0).toFixed(2)
})

const maxRate = computed(() => {
  const rates = props.item.options?.map((opt) => parseFloat(opt.intr_rate2)) || []
  return rates.length ? Math.max(...rates).toFixed(2) : '0.00'
})
</script>

<style scoped>
.item {
  background: white;
  border-radius: 16px;
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.left {
  display: flex;
  gap: 12px;
  align-items: center;
}

.left img {
  width: 40px;
  height: 40px;
}

.info h4 {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
}

.info p {
  margin: 0;
  font-size: 14px;
  color: #444;
}

.tag {
  font-size: 12px;
  background-color: #eee;
  padding: 2px 6px;
  border-radius: 4px;
  display: inline-block;
  margin-top: 4px;
}

.right {
  text-align: right;
}

.rate {
  color: #2eb474;
  font-weight: 600;
}

.base {
  font-size: 13px;
  color: #aaa;
}
</style>
