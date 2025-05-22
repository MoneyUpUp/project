<template>
  <div id="carouselExampleSlidesOnly" class="my-5 carousel slide" data-bs-ride="carousel" data-bs-interval="3000">

    <!-- 🔘 인디케이터 버튼 -->
    <div class="carousel-indicators">
      <button v-for="(image, idx) in images" :key="'indicator-' + idx" type="button"
        data-bs-target="#carouselExampleSlidesOnly" :data-bs-slide-to="idx" :class="{ active: idx === 0 }"
        :aria-current="idx === 0 ? 'true' : null" :aria-label="'Slide ' + (idx + 1)">
      </button>
    </div>

    <!-- 🖼️ 슬라이드 이미지 -->
    <div class="carousel-inner">
      <div v-for="(image, idx) in images" :key="'slide-' + idx" :class="['carousel-item', { active: idx === 0 }]">
        <img :src="image" class="d-block w-100" alt="..." />
      </div>
    </div>
  </div>
  <main>
    <homeService/>
    <homehotarticle/>
  </main>
  <footer>
    <homehotarticle/>
  </footer>
</template>

<script setup>
import homeService from '@/components/home/homeService.vue'
import homehotarticle from '@/components/home/homeHotArticle.vue'
import homefooter from '@/components/home/homeFooter.vue'
import img1 from '@/assets/banner1.png'
import img2 from '@/assets/banner2.png'


const images = [img1, img2]
</script>

<style scoped>
.carousel-indicators [data-bs-target] {
  background-color: #43B883;
}
</style>