<template>
  <div class="result-grid">
    <SearchListItem
      v-for="video in store.videoList"
      :key="video.id.videoId"
      :video="video"
    />
  </div>
</template>

<script setup>
import SearchListItem from '@/components/search/searchListItem.vue'
import { useSearchStore } from '@/stores/searchVideo'

const store = useSearchStore()
</script>

<style scoped>
.result-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
  padding: 1rem;
}

.result-grid > * {
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
  min-height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
