<template>
	<div class="back">
		<div class="map-container">
			<aside class="sidebar">
				<!-- 상단 선택 영역 -->
				<div class="search-controls">
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

					<button @click="onSearch">검색</button>
				</div>

				<!-- 스크롤 가능한 결과 영역 -->
				<div class="result-scroll">
					<ul v-if="searchResults.length" class="result-list">
						<li v-for="place in searchResults" :key="place.name" class="result-card">
							<div class="result-title">{{ place.name }}</div>
							<div class="result-address">{{ place.address }}</div>
							<div class="result-distance">📍 {{ formatDistance(place.distance) }}</div>
							<a :href="place.url" class="result-link" target="_blank">상세 보기 →</a>
						</li>
					</ul>
				</div>
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
import { formatDistance } from '@/utils/format'
import dotImage from '@/assets/dot.png'

const data = ref(null)
const searchResults = ref([])

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
const myLocation = ref(null)

onMounted(async () => {
	data.value = await (await fetch('/cities.json')).json()
	await loadKakaoMap()

	// 기본 중심 위치
	map.value = new kakao.maps.Map(document.getElementById('map'), {
		center: new kakao.maps.LatLng(37.50127380791969, 127.03958108663153),
		level: 3
	})

	// ✅ 현재 위치 가져오기
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(position => {
			const lat = position.coords.latitude
			const lng = position.coords.longitude
			const latLng = new kakao.maps.LatLng(lat, lng)
			myLocation.value = latLng

			// 🔴 내 위치 마커 추가
			const marker = new kakao.maps.Marker({
				position: latLng,
				map: map.value,
				image: new kakao.maps.MarkerImage(
					dotImage,
					new kakao.maps.Size(20, 20),
					{ offset: new kakao.maps.Point(10, 10) }
				)
			})

			// 지도 중심을 내 위치로 이동
			map.value.setCenter(latLng)
		}, () => {
			console.warn("위치 접근이 거부되었습니다.")
		})
	}
})

const onStateChange = () => {
	selectedCity.value = ''
}

const onSearch = () => {
	const keyword = `${selectedState.value} ${selectedCity.value} ${selectedBank.value}`
	if (!myLocation.value) {
		alert("위치 정보를 사용할 수 없습니다.")
		return
	}

	searchPlace(map.value, keyword, myLocation.value, results => {
		searchResults.value = results
		if (results.length === 0) alert("검색 결과가 없습니다.")
	})
}
</script>
<style scoped>
.map-container {
	display: flex;
	height: 100vh;
}

.sidebar {
	flex: 2;
	max-width: 240px;
	/* 🎯 최대 너비 제한 */
	min-width: 200px;
	margin: 2rem 3rem;
	display: flex;
	flex-direction: column;
	gap: 1rem;
}

.search-controls {
	flex-shrink: 0;
	display: flex;
	flex-direction: column;
	gap: 1rem;
}

.result-scroll {
	flex: 1;
	overflow-y: auto;
	padding-top: 1rem;
	border-top: 1px solid #ccc;
}

.result-list {
	font-size: 0.9rem;
	list-style: none;
	padding-left: 0;
	margin: 0;
}

.result-list li {
	margin-bottom: 1.5rem;
	line-height: 1.4;
}

.map-area {
	flex: 8;
	height: 100%;
	/* ✅ 전체 높이 */
	position: relative;
}

.map-box {
	width: 100%;
	height: 100%;
}

.sidebar select,
.sidebar button {
	padding: 0.5rem 0.8rem;
	/* ✅ 작고 얇게 */
	font-size: 0.9rem;
	border-radius: 6px;
	border: 1px solid #ccc;
	background-color: #fff;
	box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.sidebar select {
	background-image: url("data:image/svg+xml,%3Csvg fill='none' height='20' viewBox='0 0 24 24' width='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M7 10l5 5 5-5' stroke='%23666' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'/%3E%3C/svg%3E");
	background-repeat: no-repeat;
	background-position: right 1rem center;
	background-size: 1rem;
	padding-right: 2.5rem;
	/* 화살표 안 가려지게 */
}

.sidebar select:hover,
.sidebar button:hover {
	border-color: #007aff;
	box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.15);
}

.sidebar select:focus,
.sidebar button:focus {
	outline: none;
	border-color: #007aff;
	box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.2);
}

.sidebar button {
	background-color: #007aff;
	color: white;
	font-weight: 600;
	cursor: pointer;
}

.sidebar button:hover {
	background-color: #005fcc;
}

.result-scroll {
	flex: 1;
	overflow-y: auto;
	padding-top: 1rem;
	border-top: 1px solid #ccc;
}

/* 전체 리스트 기본 설정 */
.result-list {
	list-style: none;
	padding-left: 0;
	margin: 0;
	display: flex;
	flex-direction: column;
	gap: 1rem;
}

/* 카드 스타일 */
.result-card {
	background-color: #ffffff;
	padding: 1rem;
	border-radius: 10px;
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
	transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.result-card:hover {
	transform: translateY(-2px);
	box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.result-title {
	font-weight: 600;
	font-size: 1.1rem;
	color: #333;
	margin-bottom: 0.3rem;
}

.result-address {
	font-size: 0.95rem;
	color: #666;
	margin-bottom: 0.2rem;
}

.result-distance {
	font-size: 0.85rem;
	color: #999;
	margin-bottom: 0.5rem;
}

.result-link {
	font-size: 0.85rem;
	color: #007aff;
	text-decoration: none;
	font-weight: 500;
}

.result-link:hover {
	text-decoration: underline;
}
</style>