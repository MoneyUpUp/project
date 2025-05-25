<template>
  <div class="back">
    <div class="map-container">
      <aside class="sidebar">
        <!-- 상단 선택 영역 -->
        <SearchControls />

        <!-- 스크롤 가능한 결과 영역 -->
        <SearchResultList />
      </aside>

      <main class="map-area">
        <MapDisplay />
      </main>
    </div>
  </div>
</template>
<script setup>
import MapDisplay from '@/components/map/MapDisplay.vue'
import SearchControls from '@/components/map/SearchControls.vue'
import SearchResultList from '@/components/map/SearchResultList.vue'

import { useMapStore } from '@/stores/mapStore'
import { loadKakaoMap } from '@/utils/map/kakao.js'
import { onMounted } from 'vue'

import dotImage from '@/assets/dot.png'

const mapStore = useMapStore()

onMounted(async () => {
  mapStore.data = await (await fetch('/cities.json')).json()
  await loadKakaoMap()

  mapStore.map = new kakao.maps.Map(document.getElementById('map'), {
    center: new kakao.maps.LatLng(37.50127380791969, 127.03958108663153),
    level: 3,
  })

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude
        const lng = position.coords.longitude
        mapStore.setMyLocationOnce(lat, lng)
        
        new kakao.maps.Marker({
          position: mapStore.myLocation,
          map: mapStore.map,
          image: new kakao.maps.MarkerImage(dotImage, new kakao.maps.Size(20, 20), {
            offset: new kakao.maps.Point(10, 10),
          }),
        })

        mapStore.map.setCenter(mapStore.myLocation)
      },
      () => {
        console.warn('위치 접근이 거부되었습니다.')
      },
    )
  }
})
</script>

<style scoped>
.map-container {
  display: flex;
  height: 100vh;
}

.sidebar {
  flex: 2;
  max-width: 240px;
  min-width: 200px;
  margin: 2rem 3rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.map-area {
  flex: 8;
  height: 100%;
  position: relative;
}

.map-box {
  width: 100%;
  height: 100%;
}
</style>
