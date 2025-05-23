<template>
  <div class="deposit-list">
    <depositListItem 
      v-for="item in depositItems"
      :key="item.id"
      :item="item"
    />
  </div>
</template>

<script setup>
import depositListItem from './depositListItem.vue'
import { useProductStore } from '@/stores/products'
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router';

const store = useProductStore()
const route = useRoute();

const depositItems = ref([]);

const fetchData = async () => {
  const allData = await store.depositData()
  console.log(allData)
  const selectedBank = route.query.bank
  const selectedPeriod = route.query.period * 6


  depositItems.value = allData.filter(item => {
    const matchBank = selectedBank ? item.bank.kor_co_nm === selectedBank : true
    const matchPeriod = selectedPeriod
      ? item.options.some(opt => opt.save_trm >= selectedPeriod)
      : true
      
      return matchPeriod && matchBank
  })

  console.log(depositItems.value)
}

onMounted(fetchData)
watch(()=> route.query, fetchData)
</script>

<style scoped>
.deposit-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
