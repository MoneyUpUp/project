<template>
  <div class="result-scroll">
    <ul
      v-if="searchResults.length"
      class="result-list"
    >
      <li
        v-for="place in searchResults"
        :key="place.name"
      >
        <BaseCard>
          <div class="result-title">{{ place.name }}</div>
          <div class="result-address">{{ place.address }}</div>
          <div class="result-distance">📍 {{ formatDistance(place.distance) }}</div>
          <a
            :href="place.url"
            class="result-link"
            target="_blank"
            >상세 보기 →</a
          >
        </BaseCard>
      </li>
    </ul>
  </div>
</template>

<script setup>
import BaseCard from '@/components/base/BaseCard.vue'

import { storeToRefs } from 'pinia'

import { useMapStore } from '@/stores/mapStore'
import { formatDistance } from '@/utils/format'

const mapStore = useMapStore()
const { searchResults } = storeToRefs(mapStore)
</script>

<style scoped>
.result-scroll {
  flex: 1;
  overflow-y: auto;
  padding-top: 1rem;
  border-top: 1px solid #ccc;
}

.result-list {
  list-style: none;
  padding-left: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
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
