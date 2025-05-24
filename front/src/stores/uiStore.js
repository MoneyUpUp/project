import { useWindowSize } from '@vueuse/core'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useUiStore = defineStore('ui', () => {
  const { width } = useWindowSize()

  const isMobile = computed(() => width.value < 768)
  const isTablet = computed(() => width.value < 1024)

  // const theme = ref('light') // 기본값: light
  const theme = ref(localStorage.getItem('theme') || 'light')
  // 진입 시 테마 클래스 적용
  const html = document.documentElement
  html.classList.remove('dark', 'light')
  html.classList.add(theme.value)

  function toggleTheme() {
    const html = document.documentElement
    theme.value = theme.value === 'light' ? 'dark' : 'light'
    html.classList.remove('dark', 'light')
    html.classList.add(theme.value)
    localStorage.setItem('theme', theme.value)
    console.log('Current theme:', theme.value)
  }

  return {
    isMobile,
    isTablet,
    theme,
    toggleTheme,
  }
})
