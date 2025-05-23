<template>
    <div>
        <div class="card" style="width: 18rem;">
          <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{{video?.snippet.title}}</h5>
            <a href="#" class="card-link">+더보기</a>
          </div>
          </div>
    </div>
  </template>
  
  <script setup>
  import { RouterLink, RouterView } from 'vue-router'
  defineProps({
    video: Object
  })
  
  
  </script>
  
  <style scoped>
  
  </style>