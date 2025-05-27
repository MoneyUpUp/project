<template>
  <component :is="uiStore.isMobile ? MobileNav : DesktopNav" />
</template>

<script setup>
import DesktopNav from '@/components/layouts/nav/DesktopNav.vue'
import MobileNav from '@/components/layouts/nav/MobileNav.vue'
import { useUiStore } from '@/stores/uiStore'

const uiStore = useUiStore()
</script>
