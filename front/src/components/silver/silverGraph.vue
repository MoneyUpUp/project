<template>
  <div class="container my-5">
    <div class="w-full max-w-4xl mx-auto">
      <h2 class="text-xl font-bold mb-2">
        {{store.commodityOptions.find((opt) => opt.value === store.selectedCommodity)?.label}}
      </h2>
      <p class="text-red-500 font-semibold" v-if="store.selectedData.length">
        {{ latestPrice?.close_price.toFixed(2) }} USD
        <span v-if="change !== null && percentChange !== null"
          :class="{ 'text-green-600': change > 0, 'text-red-600': change < 0 }">
          {{ change > 0 ? '+' : '' }}{{ change.toFixed(2) }} ({{ percentChange > 0 ? '+' : ''
          }}{{ percentChange.toFixed(2) }}%)
        </span>
        <span class="text-sm text-gray-400 ml-2">
          ({{ latestPrice?.date.replaceAll('-', '.') }})
        </span>
      </p>
      <p v-else class="text-gray-500">
        데이터 없음
      </p>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed, nextTick } from 'vue' // nextTick 임포트 추가
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
    chartInstance.value.destroy();
  }

  // nextTick을 사용하여 DOM 업데이트가 완료된 후에 차트 렌더링 시도
  nextTick(() => {
    if (!chartCanvas.value) {
      console.warn('Chart canvas is not available.');
      return;
    }

    const labels = store.selectedData.map((item) => item.date);
    const prices = store.selectedData.map((item) => item.close_price);

    chartInstance.value = new Chart(chartCanvas.value, {
      type: 'line',
      data: {
        labels,
        datasets: [
          {
            label: `${store.selectedCommodity.toUpperCase()} 가격`,
            data: prices,
            borderColor: 'rgb(75, 192, 192)', // 더 부드러운 색상
            backgroundColor: (context) => {
              const chart = context.chart;
              const { ctx, chartArea } = chart;
              if (!chartArea) {
                // chartArea가 정의되지 않았을 경우 기본 색상 반환
                return 'rgba(75, 192, 192, 0.2)';
              }
              const gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
              gradient.addColorStop(0, 'rgba(75, 192, 192, 0.1)');
              gradient.addColorStop(1, 'rgba(75, 192, 192, 0.4)');
              return gradient;
            },
            fill: false, // fill 옵션을 false로 변경
            tension: 0.3, // 곡선 부드럽게
            pointRadius: 0, // 포인트 숨기기
            pointHoverRadius: 5, // 호버 시 포인트 표시
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false, // 부모 요소에 맞게 크기 조절
        clip: false, // 데이터셋 클리핑 비활성화
        plugins: {
          legend: { display: false },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(0, 0, 0, 0.7)',
            titleFont: { size: 14, weight: 'bold' },
            bodyFont: { size: 12 },
            padding: 10,
            cornerRadius: 8,
          },
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
              color: '#555',
              font: { size: 14, weight: 'bold' },
            },
            ticks: {
              color: '#666',
            },
            grid: {
              display: true,
              drawBorder: false,
              color: 'rgba(0, 0, 0, 0.05)', // 그리드 라인 연하게
            },
          },
          y: {
            title: {
              display: true,
              text: '가격 (USD)',
              color: '#555',
              font: { size: 14, weight: 'bold' },
            },
            ticks: {
              color: '#666',
            },
            grid: {
              display: true,
              drawBorder: false,
              color: 'rgba(0, 0, 0, 0.05)', // 그리드 라인 연하게
            },
            beginAtZero: false,
          },
        },
      },
    });
  });
}

onMounted(renderChart)
watch(() => store.selectedData, renderChart, { deep: true })
</script>

<style scoped>
canvas {
  max-height: 400px; /* 그래프의 최대 높이 설정 */
  width: 100%; /* 너비는 부모에 맞게 */
}
</style>
