<template>
    <div class="container">
      <BackPage />
      <div v-if="video">
        <h1>{{ decodeHTMLEntities(video.snippet.title) }}</h1>
        <p>업로드 날짜 : {{ video.snippet.publishTime.slice(0, 10) }}</p>
        <iframe width="560" height="315" :src="`https://www.youtube.com/embed/${video.id.videoId}`" frameborder="0" allowfullscreen>
        </iframe>
      </div>
      <div v-else>
        <p>동영상을 로드 중입니다...</p>
      </div>
    </div>
  </template>
  

<script setup>
import { useSearchStore } from '@/stores/searchVideo';
import { useRoute } from 'vue-router'
import {ref, watchEffect } from 'vue'

const route = useRoute()
const store = useSearchStore()
const video = ref(null)

watchEffect(()=> {
  if (store.videoList.length > 0) {
    video.value = store.showDetail(route.params.id)
  }
})

function decodeHTMLEntities(text) {
    const textarea = document.createElement('textarea');
    textarea.innerHTML = text;
    return textarea.value;
  }
  
</script>

<style scoped>

</style>