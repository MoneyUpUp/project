<template>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
import { useAccountStore } from './stores/accounts';
const store = useAccountStore()
console.log('회원가입?:',store.isLogin)
</script>
