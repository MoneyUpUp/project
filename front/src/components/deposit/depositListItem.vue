<template>
  <div class="item">
    <div class="left">
      <img src="" alt="은행로고" />
      <div class="info">
        <h4>{{ item.fin_prdt_nm }}</h4>
        <p>{{ item.bank.kor_co_rm }} · {{ item.join_member}}</p>
        <span class="tag">방문없이가입</span>
      </div>
    </div>
    <div class="right">
      <p class="rate">최고 <strong>{{ maxRate}}</strong></p>
      <p class="base">기본 {{ baseRate}}</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  item:Object
})

// 기본금리 : options[0]
const baseRate = computed(() => {
  return parseFloat(props.item.options?.[0]?.intr_rate || 0).toFixed(2)
})

// 최고 금리: options에서 intr_rate2중 가장 큰 값
const maxRate = computed(()=> {
  const rates = props.item.options?.map(opt => parseFloat(opt.intr_rate2)) || []
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
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
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
