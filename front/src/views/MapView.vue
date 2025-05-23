<template>
	<div class="back">
		<div class="map-container">
			<aside class="sidebar">
				<select v-model="selectedState" @change="onStateChange">
					<option disabled value="">도/시</option>
					<option v-for="state in states" :key="state">{{ state }}</option>
				</select>

				<select v-model="selectedCity">
					<option disabled value="">시/군/구</option>
					<option v-for="city in cities" :key="city">{{ city }}</option>
				</select>

				<select v-model="selectedBank">
					<option disabled value="">은행</option>
					<option v-for="bank in banks" :key="bank">{{ bank }}</option>
				</select>
			</aside>

			<main class="map-area">
				<div id="map" class="map-box"></div>
				<button class="search-button" @click="onSearch">현 지도에서 검색</button>
			</main>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { loadKakaoMap } from '@/utils/map/kakao.js'
import { searchPlace, clearMarkers } from '@/utils/map/mapHandler.js'

const data = ref(null)

const selectedState = ref('')
const selectedCity = ref('')
const selectedBank = ref('')
const map = ref(null)

const states = computed(() => data.value?.mapInfo.map(e => e.name) || [])
const cities = computed(() => {
	const region = data.value?.mapInfo.find(e => e.name === selectedState.value)
	return region ? region.countries : []
})
const banks = computed(() => data.value?.bankInfo || [])

onMounted(async () => {
	data.value = await (await fetch('/cities.json')).json()

	await loadKakaoMap()
	map.value = new kakao.maps.Map(document.getElementById('map'), {
		center: new kakao.maps.LatLng(37.50127380791969, 127.03958108663153),
		level: 3
	})
})

const onStateChange = () => {
	selectedCity.value = ''
}

const onSearch = async () => {
	const keyword = `${selectedState.value} ${selectedCity.value} ${selectedBank.value}`
	try {
		await searchPlace(map.value, keyword)
	} catch (e) {
		alert(e)
	}
}
</script>
<style scoped>
.map-container {
	display: flex;
	height: 100vh;
	/* background-color: #f0f0f0; */
}

.sidebar {
	width: 240px;
	/* background: #c5e8dc; */
	display: flex;
	flex-direction: column;
	padding: 2rem 1rem;
	gap: 1.2rem;
}

.sidebar select {
	padding: 0.8rem;
	font-size: 1rem;
	border: 1px solid #ccc;
	border-radius: 6px;
}

.map-area {
	height: 80%;
	flex: 1;
	position: relative;
	margin: 2rem;
	border: #007aff 2px solid;
	border-radius: 12px;
}

.map-box {
	width: 100%;
	height: 100%;
}

.search-button {
	position: absolute;
	bottom: 20px;
	left: 50%;
	transform: translateX(-50%);
	background-color: #007aff;
	color: white;
	border: none;
	border-radius: 20px;
	padding: 0.7rem 1.5rem;
	font-size: 1rem;
	cursor: pointer;
}
</style>