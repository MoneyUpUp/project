<template>
  <div class="layout-wrapper">
    <BaseNavBar />
    <RouterView />
    <!-- 테마 토글 버튼 고정 -->
    <div class="theme-toggle-btn">
      <button @click="ui.toggleTheme">123</button>
      <!-- <BaseButton @click="ui.toggleTheme">
        {{ ui.theme === 'light' ? '🌙 다크모드' : '☀️ 라이트모드' }}
      </BaseButton> -->
    </div>
  </div>
</template>

<script setup>
import BaseNavBar from '@/components/layouts/nav/BaseNavBar.vue'
import BaseButton from '@/components/base/BaseButton.vue'
import { RouterView } from 'vue-router'

import { useUiStore } from '@/stores/uiStore'

const ui = useUiStore()
</script>

<style scoped lang="scss">
@use '@/assets/styles/base/theme-vars' as *;

.layout-wrapper {
  min-height: 100vh;
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
