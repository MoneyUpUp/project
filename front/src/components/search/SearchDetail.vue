<template>
    <div class="container">
      <BackPage />
      <div v-if="video">
        <h1>{{ video.snippet.title }}</h1>
        <p>업로드 날짜 : {{ video.snippet.publishTime.slice(0, 10) }}</p>
        <iframe width="560" height="315" :src="`https://www.youtube.com/embed/${video.id.videoId}`" frameborder="0"
          allowfullscreen>
        </iframe>
      </div>
      <div v-else>
        <p>동영상을 로드 중입니다...</p>
      </div>
    </div>
  </template>
  

<script setup>

</script>

<style scoped>

</style>