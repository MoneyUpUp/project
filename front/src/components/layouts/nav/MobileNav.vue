<template>
  <nav :class="['mobile-navbar', { transparent: isHome, fixed: isHome, bordered: !isHome }]">
    <div class="mobile-header">
      <RouterLink
        to="/"
        class="logo-link"
      >
        <div class="logo">MoneyUp</div>
      </RouterLink>
      <div class="nav-actions">
        <button
          class="hamburger"
          @click="isOpen = !isOpen"
        >
          ☰
        </button>
        <img
          class="avatar-icon"
          src="@/assets/icon/basicprofile.png"
          alt="avatar"
          @click="onclick"
        />
      </div>
    </div>

    <transition name="fade">
      <ul
        v-if="isOpen"
        class="mobile-menu"
      >
        <li><RouterLink to="/product">상품</RouterLink></li>
        <li><RouterLink to="/spotAsset">현물</RouterLink></li>
        <li><RouterLink to="/map">지도</RouterLink></li>
        <li><RouterLink to="/article">커뮤니티</RouterLink></li>
        <li><RouterLink to="/searchproduct">관심종목검색</RouterLink></li>
        <li><BaseButton to="/login">로그인</BaseButton></li>
        <li>
          <BaseButton
            to="/signup"
            variant="secondary"
            >가입하기</BaseButton
          >
        </li>
      </ul>
    </transition>
  </nav>
</template>

<script setup>
import BaseButton from '@/components/base/BaseButton.vue'
import { computed, ref } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'

const isOpen = ref(false)
const route = useRoute()
const router = useRouter()
const isHome = computed(() => route.path === '/')
const isLoggedIn = ref(false) // Replace with real auth logic later

const onclick = () => {
  const destination = isLoggedIn.value ? '/profile' : '/login'
  router.push(destination)
}
</script>

<style scoped lang="scss">
@use '@/assets/styles/utils/variables' as *;

.mobile-navbar {
  width: 100%;
  font-family: $font-base;
  z-index: 1000;

  &.transparent {
    background-color: rgba(255, 255, 255, 0.3);
  }

  &.fixed {
    position: fixed;
    top: 0;
    left: 0;
  }

  &.bordered {
    border-bottom: 1px solid #e0e0e0;
  }
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

.nav-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.avatar-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  margin-left: auto;
  cursor: pointer;
}
</style>
