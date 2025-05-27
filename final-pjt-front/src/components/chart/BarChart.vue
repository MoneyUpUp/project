<template>
  <canvas ref="barChartCanvas"></canvas>
</template>

<script setup>
import { ref, onMounted, watch, onBeforeUnmount } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const props = defineProps({
  chartData: {
    type: Object,
    required: true,
  },
  options: {
    type: Object,
    default: () => ({}),
  },
});

const barChartCanvas = ref(null);
let chartInstance = null;

const renderChart = () => {
  if (chartInstance) {
    chartInstance.destroy();
  }

  const ctx = barChartCanvas.value.getContext('2d');
  chartInstance = new Chart(ctx, {
    type: 'bar',
    data: props.chartData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      ...props.options,
    },
  });
};

onMounted(() => {
  renderChart();
});

watch(() => props.chartData, () => {
  renderChart();
}, { deep: true });

onBeforeUnmount(() => {
  if (chartInstance) {
    chartInstance.destroy();
  }
});
</script>

<style scoped>
canvas {
  max-height: 400px; /* Adjust as needed */
}
</style>
