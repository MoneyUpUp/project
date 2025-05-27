<template>
  <nav :class="['mobile-navbar', { transparent: isHome, fixed: isHome, bordered: !isHome }]">
    <div class="mobile-header">
      <RouterLink
        to="/"
        class="logo-link"
        @click="closeMenu"
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
        <li>
          <RouterLink
            to="/product"
            @click="closeMenu"
            >상품</RouterLink
          >
        </li>
        <li>
          <RouterLink
            to="/spotAsset"
            @click="closeMenu"
            >현물</RouterLink
          >
        </li>
        <li>
          <RouterLink
            to="/map"
            @click="closeMenu"
            >지도</RouterLink
          >
        </li>
        <li>
          <RouterLink
            to="/article"
            @click="closeMenu"
            >커뮤니티</RouterLink
          >
        </li>
        <li>
          <RouterLink
            to="/searchproduct"
            @click="closeMenu"
            >관심종목검색</RouterLink
          >
        </li>
      </ul>
    </transition>
  </nav>
</template>

<script setup>
import { computed, ref } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'

const isOpen = ref(false)
const route = useRoute()
const router = useRouter()
const isHome = computed(() => route.path === '/')
const isLoggedIn = ref(false) // Replace with real auth logic later

const onclick = () => {
  const destination = isLoggedIn.value ? '/profile' : '/login'
  closeMenu()
  router.push(destination)
}

const closeMenu = () => {
  isOpen.value = false
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
  position: relative;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo {
  font-weight: 900;
  font-size: 20px;
  color: $primary-500;
  text-align: center;
}

.logo-link {
  text-decoration: none;
}

.hamburger {
  position: absolute;
  left: 1rem;
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
  position: absolute;
  right: 1rem;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  margin-left: auto;
  cursor: pointer;
}
</style>
