<template>
    <div>
        <div class="card" style="width: 18rem;">
          <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{{decodeHTMLEntities(video?.snippet.title) }}</h5>
            <a @click="onclick" href="#" class="card-link">+더보기</a>
          </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import { RouterLink, RouterView, useRouter } from 'vue-router'
  defineProps({
    video: Object
  })

  const router = useRouter()

  function onClick() {
    router.push('/searchproduct/detail')
  }

  function decodeHTMLEntities(text) {
    const textarea = document.createElement('textarea');
    textarea.innerHTML = text;
    return textarea.value;
  }
  
  
  </script>
  
  <style scoped>
  
  </style>