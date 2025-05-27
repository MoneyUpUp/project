<template>
  <div>
    <div class="banner-container">
      <transition name="fade" mode="out-in">
        <img :key="currentBanner" :src="currentBanner" class="banner-image" alt="Banner" ref="mainBannerImageRef" />
      </transition>
      <div class="banner-text" :style="{ opacity: bannerTextOpacity, transition: 'opacity 0.5s ease' }">MoneyUp</div>
    </div>
    <main>
      <homeService/>
      <homehotarticle/>
    </main>
    <footer>
      <homefooter class="footer"/>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import homeService from '@/components/home/homeService.vue'
import homehotarticle from '@/components/home/homeHotArticle.vue'
import homefooter from '@/components/home/homeFooter.vue'

// Banner 이미지 임포트
import banner1 from '@/assets/banner/mainbanner.gif'
// import banner2 from '@/assets/banner/54cbe4219310031.67afab66455f0.gif' // 파일 경로 오류로 주석 처리
import banner3 from '@/assets/banner/393174217783407.6796c20101198.gif'
import banner4 from '@/assets/banner/d5bf18219310031.67afad9f6f486.gif' // 다시 포함

const banners = [banner1, banner3, banner4] // banner2 제외, banner4 포함
const currentBannerIndex = ref(0)
let bannerInterval = null

const currentBanner = computed(() => banners[currentBannerIndex.value])

const bannerTextOpacity = ref(1)
const mainBannerImageRef = ref(null)

const handleScroll = () => {
  if (mainBannerImageRef.value) {
    const bannerRect = mainBannerImageRef.value.getBoundingClientRect()
    const bannerHeight = mainBannerImageRef.value.offsetHeight
    const navBarHeight = 60; 

    if (bannerRect.bottom < navBarHeight + (bannerHeight * 0.3) ) {
      bannerTextOpacity.value = 0
    } else {
      bannerTextOpacity.value = 1
    }
  }
}

const startBannerRotation = () => {
  if (banners.length > 1) {
    bannerInterval = setInterval(() => {
      currentBannerIndex.value = (currentBannerIndex.value + 1) % banners.length
    }, 3000) 
  } else if (banners.length === 1) {
    currentBannerIndex.value = 0;
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  handleScroll()
  startBannerRotation()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  if (bannerInterval) {
    clearInterval(bannerInterval)
  }
})
</script>

<style scoped>
.banner-container {
  width: 100%;
  height: 1080px; 
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative; 
  overflow: hidden; 
}

.banner-text {
  position: absolute; 
  top: 50%; 
  left: 50%;
  transform: translate(-50%, -50%);
  color: #43B883; 
  font-size: 5rem; 
  font-weight: 700;
  text-align: center;
  letter-spacing: -0.05em; 
  z-index: 1; 
}

.banner-image {
  width: 1920px; 
  height: 1080px; 
  object-fit: cover; 
  position: absolute; 
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.footer {
  background-color: #43B883;
  color: black;
  height: 195px;
  left: 0;
  width: 100%;
  position: relative;
  transform: translateY(+10%);
}
</style>
