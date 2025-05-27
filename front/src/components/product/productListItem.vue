<template>
  <BaseCard style="cursor: pointer">
    <div class="item">
      <div class="left">
        <img
          :src="item.bank.logo"
          :alt="item.bank.kor_co_nm"
          @error="onImgError"
        />
        <div class="info">
          <h4>{{ item.fin_prdt_nm }}</h4>
          <p>{{ item.bank.kor_co_nm }} · {{ item.join_member }}</p>
          <div class="tags">
            <span
              v-for="(way, index) in Array.isArray(item.join_way) ? item.join_way : [item.join_way]"
              :key="index"
              class="tag"
            >
              {{ way }}
            </span>
          </div>
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
import { useProductStore } from '@/stores/productStore'
import { computed } from 'vue'

const props = defineProps({
  item: Object,
})

const productStore = useProductStore()

const filteredOptions = computed(() => {
  const terms = [6, 12, 24, 36]
  const selectedTerm = terms[productStore.selectedIndex]
  const options = props.item.options || []

  // Try to find exact match first
  let filtered = options.filter((opt) => opt.save_trm === selectedTerm)

  // If no match, fallback to the smallest available
  if (filtered.length === 0) {
    filtered = [...options].sort((a, b) => a.save_trm - b.save_trm)
  }

  return filtered
})

const baseRate = computed(() => {
  return parseFloat(filteredOptions.value?.[0]?.intr_rate || 0).toFixed(2)
})

const maxRate = computed(() => {
  const rates = filteredOptions.value.map((opt) => parseFloat(opt.intr_rate2 || 0))
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

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-top: 4px;
}

.tag {
  font-size: 12px;
  background-color: #eee;
  padding: 2px 6px;
  border-radius: 4px;
  display: inline-block;
  margin: 4px 4px 0 0;
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
