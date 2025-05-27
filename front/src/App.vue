<template>
  <div :class="{'app-container': !isAuthRoute, 'auth-container': isAuthRoute}">
    <RouterView />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { RouterView, useRoute } from 'vue-router'
import { useAccountStore } from './stores/accounts';

const store = useAccountStore()
console.log('회원가입?:',store.isLogin)
const route = useRoute()

// 현재 경로가 로그인 또는 회원가입 페이지인지 확인
const isAuthRoute = computed(() => {
  return route.path.startsWith('/login') || route.path.startsWith('/signup');
})
</script>

<style scoped>
.app-container {
  padding-top: 60px; /* 네비게이션 바 높이만큼 패딩 추가 */
}

.auth-container {
  padding-top: 0; /* 로그인/회원가입 페이지는 패딩 없음 */
}
</style>
