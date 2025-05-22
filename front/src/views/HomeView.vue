<template>
	<div>
		<h1>home</h1>
		<div class="carousel">
    <div class="carousel-track" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
      <div class="carousel-slide" v-for="(image, index) in images" :key="index">
        <img :src="image" alt="캐러셀 이미지" />
      </div>
    </div>

    <button class="carousel-btn prev" @click="prevSlide">‹</button>
    <button class="carousel-btn next" @click="nextSlide">›</button>
  </div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import banner1 from '@/assets/banner1.png'
import banner2 from '@/assets/banner2.png'

const images = [banner1, banner2]

const currentIndex = ref(0)

const prevSlide = () => {
  currentIndex.value = (currentIndex.value + images.length - 1) % images.length
}

const nextSlide = () => {
  currentIndex.value = (currentIndex.value + 1) % images.length
}
</script>

<style scoped>
.carousel {
  position: relative;
  width: auto;
  height: auto;
  overflow: hidden;
  margin: 0 auto;
}

.carousel-track {
  display: flex;
  transition: transform 0.5s ease-in-out;
  height: 100%;
}

.carousel-slide {
  min-width: 100%;
  height: 100%;
  flex-shrink: 0;
}

.carousel-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.6);
  border: none;
  font-size: 32px;
  padding: 8px 12px;
  cursor: pointer;
  z-index: 2;
  border-radius: 50%;
  transition: background 0.2s;
}

.carousel-btn:hover {
  background: rgba(255, 255, 255, 0.9);
}

.prev {
  left: 16px;
}

.next {
  right: 16px;
}
</style>