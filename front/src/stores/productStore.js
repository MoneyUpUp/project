import { BANK_OPTIONS } from '@/constants/banks'
import {
  matchesBank,
  matchesPeriod,
  matchesType,
  parseProductData,
} from '@/utils/product/productFilters'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useProductStore = defineStore('product', () => {
  const selectedBank = ref('all')
  const selectedIndex = ref(0)
  const selectedTypes = ref(['deposit', 'saving'])
  const allItems = ref([])

  const bankOptions = computed(() => BANK_OPTIONS)

  const filteredItems = computed(() =>
    allItems.value.filter(
      (item) =>
        matchesType(item, selectedTypes.value) &&
        matchesBank(item, selectedBank.value) &&
        matchesPeriod(item, selectedIndex.value),
    ),
  )

  async function fetchAllProducts() {
    allItems.value = []

    try {
      const res = await fetch('/product.json')
      const data = await res.json()

      const depositData = parseProductData(data.deposit_products || [], 'deposit')
      const savingData = parseProductData(data.saving_products || [], 'saving')

      allItems.value.push(...depositData, ...savingData)
    } catch (err) {
      console.error('❌ productData 파싱 오류:', err)
      allItems.value = []
    }
  }

  return {
    selectedBank,
    selectedIndex,
    selectedTypes,
    bankOptions,
    filteredItems,
    fetchAllProducts,
  }
})
