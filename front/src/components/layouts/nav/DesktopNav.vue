<template>
  <nav class="navbar">
    <div class="container">
      <div class="left-section">
        <RouterLink
          to="/"
          class="logo-link"
        >
          <div class="logo">MoneyUp</div>
        </RouterLink>

        <ul class="nav-links">
          <li><RouterLink to="/product">상품</RouterLink></li>
          <li><RouterLink to="/spotAsset">현물</RouterLink></li>
          <li><RouterLink to="/map">지도</RouterLink></li>
          <li><RouterLink to="/article">커뮤니티</RouterLink></li>
          <li><RouterLink to="/searchproduct">관심종목검색</RouterLink></li>
        </ul>
      </div>

      <div class="right-section">
        <BaseButton to="/login">로그인</BaseButton>
        <BaseButton
          to="/signup"
          variant="secondary"
          >가입하기</BaseButton
        >
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import BaseButton from '@/components/base/BaseButton.vue'
</script>

<style scoped lang="scss">
@use '@/assets/styles/utils/variables' as *;

// .navbar {
//   width: 100%;
//   height: 60px;
//   display: flex;
//   align-items: center;
//   padding: 0 $space-xl * 10;
//   background-color: white;
//   border-bottom: 1px solid #e0e0e0;
//   font-family: $font-base;
// }

// .left-section {
//   display: flex;
//   align-items: center;
//   gap: 40px;
// }

// .logo {
//   font-weight: 900;
//   font-size: 24px;
//   line-height: 36px;
//   color: $primary-500;
// }

// .logo-link {
//   text-decoration: none;
// }

// .nav-links {
//   display: flex;
//   list-style: none;
//   gap: 24px;
//   margin: 0;
//   padding: 0;
// }

// .nav-links li {
//   cursor: pointer;
//   font-weight: 600;
//   font-size: 16px;
//   color: $primary-500;
// }

// .nav-links a {
//   text-decoration: none;
//   color: inherit;
// }

// .right-section {
//   display: flex;
//   gap: 12px;
//   align-items: center;
//   margin-left: auto;
// }

.navbar {
  width: 100%;
  background-color: white;
  border-bottom: 1px solid #e0e0e0;
  font-family: $font-base;
}

.wrapper {
  max-width: 1280px;
  margin: 0 auto;
  height: 60px;
  padding: 0 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.left-section {
  display: flex;
  align-items: center;
  gap: 40px;
}

.logo {
  font-weight: 900;
  font-size: 24px;
  line-height: 36px;
  color: $primary-500;
}

.logo-link {
  text-decoration: none;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 24px;
  margin: 0;
  padding: 0;
}

.nav-links li {
  cursor: pointer;
  font-weight: 600;
  font-size: 16px;
  color: $primary-500;
}

.nav-links a {
  text-decoration: none;
  color: inherit;
}

.right-section {
  display: flex;
  gap: 12px;
  align-items: center;
}
</style>
