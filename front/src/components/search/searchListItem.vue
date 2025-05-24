<template>
    <div>
        <div class="card" style="width: 18rem;">
          <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{{decodeHTMLEntities(video?.snippet.title) }}</h5>
            <button @click="onClick" class="card-link" style="background: none; border: none; padding: 0; color: blue; text-decoration: underline; cursor: pointer;">
              +더보기
            </button>
          </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import { RouterLink, RouterView, useRouter } from 'vue-router'
  const props = defineProps({
    video: Object
  })

  const router = useRouter()

  function onClick() {
    console.log('버튼클릭')
    router.push({name:'search-detail', params:{id: props.video?.id?.videoId}})
  }

  function decodeHTMLEntities(text) {
    const textarea = document.createElement('textarea');
    textarea.innerHTML = text;
    return textarea.value;
  }
  
  
  </script>
  
  <style scoped>
  
  </style>