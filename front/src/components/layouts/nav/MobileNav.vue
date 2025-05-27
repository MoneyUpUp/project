<template>
  <nav class="mobile-navbar">
    <div class="mobile-header">
      <RouterLink to="/" class="logo-link">
        <div class="logo">MoneyUp</div>
      </RouterLink>
      <button class="hamburger" @click="isOpen = !isOpen">☰</button>
    </div>

    <transition name="fade">
      <ul v-if="isOpen" class="mobile-menu">
        <li><RouterLink to="/product">상품</RouterLink></li>
        <li><RouterLink to="/spotAsset">현물</RouterLink></li>
        <li><RouterLink to="/map">지도</RouterLink></li>
        <li><RouterLink to="/article">커뮤니티</RouterLink></li>
        <li><RouterLink to="/searchproduct">관심종목검색</RouterLink></li>
        <li><BaseButton to="/login">로그인</BaseButton></li>
        <li><BaseButton to="/signup" variant="secondary">가입하기</BaseButton></li>
      </ul>
    </transition>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import BaseButton from '@/components/base/BaseButton.vue'

const isOpen = ref(false)
</script>

<style scoped lang="scss">
@use '@/assets/styles/utils/variables' as *;

.mobile-navbar {
  width: 100%;
  background-color: white;
  border-bottom: 1px solid #e0e0e0;
  font-family: $font-base;
  position: fixed; /* 내비게이션 바 고정 */
  top: 0;
  left: 0;
  z-index: 1000; /* 다른 콘텐츠 위에 오도록 z-index 설정 */
}

.mobile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.logo {
  font-weight: 900;
  font-size: 20px;
  color: $primary-500;
}

.logo-link {
  text-decoration: none;
}

.hamburger {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.mobile-menu {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
  list-style: none;
  background: #f9f9f9;

  li {
    font-weight: 600;
    font-size: 1rem;
    color: $primary-700;
  }

  a {
    text-decoration: none;
    color: inherit;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
