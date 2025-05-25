<template>
  <div class="container my-5">
    <div class="w-full max-w-4xl mx-auto">
      <h2 class="text-xl font-bold mb-2">
        {{ store.commodityOptions.find((opt) => opt.value === store.selectedCommodity)?.label }}
        가격 (USD)
      </h2>
      <p
        class="text-red-500 font-semibold"
        v-if="store.selectedData.length"
      >
        {{ latestPrice?.close_price.toFixed(2) }} USD
        <span
          v-if="change !== null && percentChange !== null"
          :class="{ 'text-green-600': change > 0, 'text-red-600': change < 0 }"
        >
          {{ change > 0 ? '+' : '' }}{{ change.toFixed(2) }} ({{ percentChange > 0 ? '+' : ''
          }}{{ percentChange.toFixed(2) }}%)
        </span>
        <span class="text-sm text-gray-400 ml-2">
          ({{ latestPrice?.date.replaceAll('-', '.') }})
        </span>
      </p>
      <p
        v-else
        class="text-gray-500"
      >
        데이터 없음
      </p>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue'
import { Chart, registerables } from 'chart.js'
import { useSpotAssetStore } from '@/stores/spotAssetStore'

Chart.register(...registerables)

const chartCanvas = ref(null)
const chartInstance = ref(null)
const store = useSpotAssetStore()

const latestPrice = computed(() => {
  const data = store.selectedData
  return data.length ? data[data.length - 1] : null
})

const change = computed(() => {
  const data = store.selectedData
  if (data.length < 2) return null
  return data[data.length - 1].close_price - data[0].close_price
})

const percentChange = computed(() => {
  const data = store.selectedData
  if (data.length < 2) return null
  return (change.value / data[0].close_price) * 100
})

function renderChart() {
  if (chartInstance.value) {
    chartInstance.value.destroy()
  }

  const labels = store.selectedData.map((item) => item.date)
  const prices = store.selectedData.map((item) => item.close_price)

  chartInstance.value = new Chart(chartCanvas.value, {
    type: 'line',
    data: {
      labels,
      datasets: [
        {
          label: `${store.selectedCommodity.toUpperCase()} 가격`,
          data: prices,
          borderColor: 'rgba(54, 162, 235, 1)',
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          fill: true,
          tension: 0.4,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: { mode: 'index', intersect: false },
      },
      interaction: {
        mode: 'index',
        intersect: false,
      },
      scales: {
        x: {
          title: {
            display: true,
            text: '날짜',
          },
        },
        y: {
          title: {
            display: true,
            text: '가격 (USD)',
          },
          beginAtZero: false,
        },
      },
    },
  })
}

onMounted(renderChart)
watch(() => store.selectedData, renderChart, { deep: true })
</script>
