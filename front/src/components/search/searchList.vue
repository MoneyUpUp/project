<template>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div
        class="col" 
        v-for="video in store.videoList"
        :key="video.id.videoId"
      >
        <searchListItem :video="video"/>
      </div>
    </div>
  </template>
  
  <script setup>
  import searchListItem from '@/components/search/searchListItem.vue';
  import { useSearchStore } from '@/stores/searchVideo';
  
  const store = useSearchStore()
  console.log(store.videoList)
  
  
  </script>
  
  <style scoped>
  
  </style>