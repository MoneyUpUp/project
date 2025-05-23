<template>
    <div class="container my-5">
        <div class="w-full max-w-4xl mx-auto">
            <h2 class="text-xl font-bold mb-2">XAG/USD - 은 현물가격 미국 달러</h2>
            <p class="text-red-500 font-semibold">
                {{ currentPrice }} USD
                <span :class="{ 'text-green-600': change > 0, 'text-red-600': change < 0 }">
                    {{ change > 0 ? '+' : '' }}{{ change.toFixed(4) }} ({{ percentChange > 0 ? '+' : '' }}{{
                        percentChange.toFixed(2) }}%)
                </span>
            </p>
            <canvas ref="chartCanvas"></canvas>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

const chartCanvas = ref(null);

const labels = ['18:00', '21:00', '0:00', '03:00', '06:00', '09:00', '11:00'];
const prices = [32.75, 32.90, 33.20, 33.50, 33.00, 33.05, 33.1085];

const currentPrice = prices[prices.length - 1];
const change = currentPrice - prices[0];
const percentChange = (change / prices[0]) * 100;

onMounted(() => {
    new Chart(chartCanvas.value, {
        type: 'line',
        data: {
            labels,
            datasets: [{
                label: 'XAG/USD',
                data: prices,
                borderColor: 'rgba(255, 99, 132, 1)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: { mode: 'index', intersect: false },
            },
            interaction: {
                mode: 'index',
                intersect: false
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: '시간'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: '가격 (USD)'
                    },
                    beginAtZero: false
                }
            }
        }
    });
});
</script>

<style scoped>
canvas {
    max-height: 400px;
}
</style>
