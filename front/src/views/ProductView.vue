<template>
  <div class="container">
    <ProductFilterPanel />

    <main class="main-content">
      <ProductAdvancedFilter class="filter-sidebar" />
      <section class="product-list-section">
        <div class="scroll-area">
          <ProductList
            :items="productStore.filteredItems"
            @select="selectedItem = $event"
          />
        </div>
      </section>
    </main>
    <!-- 모달 -->
    <ProductModal
      v-if="selectedItem"
      :product="selectedItem"
      @close="selectedItem = null"
    />
  </div>
</template>
<script setup>
// ✅ 필요한 모듈 불러오기
import ProductAdvancedFilter from '@/components/product/ProductAdvancedFilter.vue'
import ProductFilterPanel from '@/components/product/ProductFilterPanel.vue'
import ProductList from '@/components/product/ProductList.vue'
import ProductModal from '@/components/product/ProductModal.vue'
import { useProductStore } from '@/stores/productStore'
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

// ✅ 상태 저장소 가져오기
const productStore = useProductStore()
const route = useRoute()
const router = useRouter()
const selectedItem = ref(null)
// ✅ 예금/적금 탭 전환 핸들러
const setType = (value) => {
  productStore.type = value
  router.push({
    path: `/product/${value}`,
    query: {
      bank: productStore.selectedBank,
      period: productStore.selectedIndex,
    },
  })
}

// ✅ 슬라이더 스타일 계산
const getSliderBackground = computed(() => {
  const percent = (productStore.selectedIndex / 3) * 100
  return `linear-gradient(to right, #43B883 0%, #43B883 ${percent}%, #D9F1E6 ${percent}%, #D9F1E6 100%)`
})

// ✅ 최초 데이터 패치
onMounted(() => {
  productStore.fetchAllProducts()
})
</script>

<style scoped>
:root {
  --offset-top: 160px;
}
.scroll-area {
  flex: 1;
  overflow-y: auto;
  padding-right: 4px;
}
.main-content {
  display: flex;
  gap: 32px;
  height: calc(100vh - var(--offset-top));
}

.filter-sidebar {
  width: 240px;
  min-width: 200px;
  background-color: #f9f9f9;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1rem;
}
.product-list-section {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
</style>
