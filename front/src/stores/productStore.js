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
  const sortOption = ref('name')
  const allItems = ref([])

  const bankOptions = computed(() => BANK_OPTIONS)

  const filteredItems = computed(() => {
    const filtered = allItems.value.filter(
      (item) =>
        matchesType(item, selectedTypes.value) &&
        matchesBank(item, selectedBank.value) &&
        matchesPeriod(item, selectedIndex.value),
    )

    if (sortOption.value === 'rate') {
      return filtered.sort((a, b) => {
        const maxRateA = Math.max(...(a.options?.map((opt) => parseFloat(opt.intr_rate2)) || [0]))
        const maxRateB = Math.max(...(b.options?.map((opt) => parseFloat(opt.intr_rate2)) || [0]))
        return maxRateB - maxRateA
      })
    }

    // 기본: 이름순
    return filtered.sort((a, b) => a.fin_prdt_nm.localeCompare(b.fin_prdt_nm))
  })

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
    sortOption,
    bankOptions,
    filteredItems,
    fetchAllProducts,
  }
})
