<template>
  <div class="layout-wrapper">
    <BaseNavBar />

    <div class="content-area">
      <RouterView />
      <!-- 테마 토글 버튼 고정 -->
      <div class="theme-toggle-btn">
        <button @click="ui.toggleTheme">123</button>
        <!-- <BaseButton @click="ui.toggleTheme">
        {{ ui.theme === 'light' ? '🌙 다크모드' : '☀️ 라이트모드' }}
      </BaseButton> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import BaseNavBar from '@/components/layouts/nav/BaseNavBar.vue'
import { RouterView } from 'vue-router'

import { useUiStore } from '@/stores/uiStore'

const ui = useUiStore()
</script>

<style scoped lang="scss">
@use '@/assets/styles/base/theme-vars' as *;

.layout-wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh; // 전체 화면
}

.content-area {
  flex: 1;
  overflow-y: auto;
  background: var(--bg-color);
  color: var(--text-color);
}
.theme-toggle-btn {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  z-index: 999;
}
</style>
