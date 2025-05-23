<template>
    <div class="deposit-list">
      <productListItem 
        v-for="item in items"
        :key="item.id"
        :item="item"
      />
    </div>
  </template>
  
  <script setup>
  import productListItem from './productListItem.vue'
  import { useProductStore } from '@/stores/products'
  import { useRoute } from 'vue-router';
  import { defineProps } from 'vue'
  
  const route = useRoute();
  const props = defineProps({
  items: Array
})
  

  </script>
  
  <style scoped>
  .deposit-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  </style>
  