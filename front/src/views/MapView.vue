<template>
  <div class="back">
    <div class="map-container">
      <aside class="sidebar">
        <!-- 뷰 전환에 따라 컴포넌트 렌더링 -->
        <SearchControls/>
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

  // 지도 이동 시작 시 버튼 표시
  kakao.maps.event.addListener(mapStore.map, 'dragstart', function() {
    mapStore.showSearchButton = true;
  });

  // 지도 이동 종료 시 버튼 숨김 (사용자 요청에 따라 이 로직을 제거하거나 수정해야 함)
  // 현재는 스크롤 멈추면 사라지는 문제 해결을 위해 idle 이벤트에서 숨기는 로직을 제거합니다.
  // kakao.maps.event.addListener(mapStore.map, 'idle', function() {
  //   mapStore.showSearchButton = false;
  // });

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
  height: calc(100vh - 60px); /* 네비게이션 바 높이(60px)를 제외한 높이 */
  margin-top: 60px; /* 네비게이션 바 아래로 이동 */
  padding: 20px; /* 전체 컨테이너에 패딩 추가 */
  box-sizing: border-box; /* 패딩이 너비에 포함되도록 설정 */
}

.sidebar {
  flex: 2;
  max-width: 280px; /* 사이드바 최대 너비 조정 */
  min-width: 250px; /* 사이드바 최소 너비 조정 */
  margin: 0 20px 0 0; /* 오른쪽 마진만 추가 */
  display: flex;
  flex-direction: column;
  gap: 1.5rem; /* 컴포넌트 간 간격 조정 */
  background-color: #ffffff; /* 사이드바 배경색 */
  border-radius: 12px; /* 둥근 모서리 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
  padding: 20px; /* 사이드바 내부 패딩 */
  overflow-y: auto; /* 내용이 넘칠 경우 스크롤 */
}

.map-area {
  flex: 8;
  height: 100%;
  position: relative;
  overflow: hidden; /* 지도가 둥근 모서리 밖으로 나가지 않도록 */
  background-color: #ffffff; /* 지도 영역 배경색 */
  border-radius: 12px; /* 둥근 모서리 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
}

</style>
