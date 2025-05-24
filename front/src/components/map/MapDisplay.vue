<template>
  <div
    id="map"
    class="map-box"
  ></div>
  <button
    class="search-button"
    @click="mapStore.onSearch"
  >
    현 지도에서 검색
  </button>
</template>

<script setup>
import { useMapStore } from '@/stores/mapStore'
const mapStore = useMapStore()
</script>

<style scoped>
.map-area {
  flex: 8;
  height: 100%;
  position: relative;
}

.map-box {
  width: 100%;
  height: 100%;
}

.search-button {
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  padding: 0.5rem 1rem;
  background-color: #007aff;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #005fcc;
}
</style>
