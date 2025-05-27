<template>
  <div class="full-width">
    <h3>찜 목록</h3>
    <AccessionList
      :items="store.favoriteList"
      @update:selected-items="handleSelectedItemsChange"
    />
    <div class="button-right">
      <DeleteButton @click="handleDeleteSelected" />
    </div>

    <hr />

    <h3>이자율 비교</h3>
    <div class="chart-container">
      <BarChart
        :key="selectedFavoriteItems.length"
        :chartData="interestRateChartData"
      />
    </div>
  </div>
</template>

<script setup>
import DeleteButton from '@/components/button/DeleteButton.vue'
import BarChart from '@/components/chart/BarChart.vue'
import { useFavoriteStore } from '@/stores/favorite'
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import AccessionList from './accession/AccessionList.vue'

const store = useFavoriteStore()
const route = useRoute()
const selectedFavoriteItems = ref([])

const handleSelectedItemsChange = (items) => {
  console.log(`--------------------items: ${items}`)
  selectedFavoriteItems.value = items
  console.log('AccessionProduct - selectedFavoriteItems updated:', selectedFavoriteItems.value)
}

const handleDeleteSelected = async () => {
  try {
    console.log('선택된 아이템')
    console.log(selectedFavoriteItems.value)
    await store.deleteFavorites(selectedFavoriteItems.value)
    alert('선택한 관심 상품이 삭제되었습니다.')
    selectedFavoriteItems.value = []
  } catch (err) {
    alert('삭제 중 오류가 발생했습니다.')
  }
}

const interestRateChartData = computed(() => {
  const labels = selectedFavoriteItems.value.map((item) => item.fin_prdt_nm)
  const baseRates = selectedFavoriteItems.value.map((item) => item.options?.[0]?.intr_rate ?? 0)
  const maxRates = selectedFavoriteItems.value.map((item) => item.options?.[0]?.intr_rate2 ?? 0)

  console.log('Chart Data Labels:', labels)
  console.log('Base Rates:', baseRates)
  console.log('Max Rates:', maxRates)

  return {
    labels,
    datasets: [
      {
        label: '기본 이자율',
        backgroundColor: '#42A5F5',
        data: baseRates,
      },
      {
        label: '최고 우대 이자율',
        backgroundColor: '#FFC107',
        data: maxRates,
      },
    ],
  }
})

onMounted(() => {
  store.getFavoriteList()
  console.log('AccessionProduct - favoriteList onMounted:', store.favoriteList)
})

watch(
  () => store.favoriteList,
  (newVal) => {
    console.log('AccessionProduct - store.favoriteList changed:', newVal)
    selectedFavoriteItems.value = selectedFavoriteItems.value.filter(
      (selected) =>
        (newVal.favorite_deposits || []).some(
          (item) => item.fin_prdt_cd === selected.fin_prdt_cd && selected.type === 'deposit',
        ) ||
        (newVal.favorite_savings || []).some(
          (item) => item.fin_prdt_cd === selected.fin_prdt_cd && selected.type === 'saving',
        ) ||
        (newVal.favorite_assets || []).some(
          (item) => item.fin_prdt_cd === selected.fin_prdt_cd && selected.type === 'asset',
        ),
    )
  },
  { deep: true },
)
</script>

<style scoped>
.full-width {
  margin-top: 8%;
}

.button-right {
  display: flex;
  justify-content: flex-end;
  margin: 1rem 0;
}

.chart-container {
  width: 100%;
  height: 400px;
}
</style>
