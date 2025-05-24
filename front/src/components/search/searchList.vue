<template>
    <div class="row row-cols-1 row-cols-md-4 g-2">
      <div
        class="col" 
        v-for="video in store.videoList"
        :key="video.id.videoId"
      >
        <SearchListItem :video="video"/>
      </div>
    </div>
  </template>
  
  <script setup>
  import SearchListItem from '@/components/search/SearchListItem.vue';
  import { useSearchStore } from '@/stores/searchVideo';
  
  const store = useSearchStore()
  
  
  </script>
  
  <style scoped>
  
  </style>