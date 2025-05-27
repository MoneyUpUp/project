<template>
  <div class="home-wrapper">
    <div class="banner-container">
      <transition
        name="fade"
        mode="out-in"
      >
        <img
          :key="currentBanner"
          :src="currentBanner"
          class="banner-image"
          alt="Banner"
          ref="mainBannerImageRef"
        />
      </transition>
      <div
        class="banner-text"
        :style="{ opacity: bannerTextOpacity, transition: 'opacity 0.5s ease' }"
      >
        MoneyUp
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, ref } from 'vue'

import banner2 from '@/assets/banner/393174217783407.6796c20101198.gif'
import banner3 from '@/assets/banner/d5bf18219310031.67afad9f6f486.gif'
import banner1 from '@/assets/banner/mainbanner.gif'

const banners = [banner1, banner2, banner3]

const currentBannerIndex = ref(0)
const bannerTextOpacity = ref(1)
const mainBannerImageRef = ref(null)

let bannerInterval = null

const currentBanner = computed(() => banners[currentBannerIndex.value])

const handleScroll = () => {
  if (mainBannerImageRef.value) {
    const bannerRect = mainBannerImageRef.value.getBoundingClientRect()
    const bannerHeight = mainBannerImageRef.value.offsetHeight
    const navBarHeight = 60

    if (bannerRect.bottom < navBarHeight + bannerHeight * 0.3) {
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
    currentBannerIndex.value = 0
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
.home-wrapper {
  height: 100vh;
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
}
.banner-container {
  width: 100vw;
  height: 100vh;
  position: relative;
  flex-shrink: 0;
  scroll-snap-align: start;
}

.banner-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #43b883;
  font-size: 5rem;
  font-weight: 700;
  text-align: center;
  letter-spacing: -0.05em;
  z-index: 1;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.scroll-indicator {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 2rem;
  color: white;
  animation: bounce 1.5s infinite;
  z-index: 2;
  pointer-events: none;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateX(-50%) translateY(0);
  }
  50% {
    transform: translateX(-50%) translateY(10px);
  }
}

.home-section {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  scroll-snap-align: start;
  background-color: white;
}

.home-section.alt {
  background-color: #f9f9f9;
}
</style>
