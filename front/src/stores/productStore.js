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

    const [depositRes, savingRes] = await Promise.all([
      fetch('/deposit.json'),
      fetch('/saving.json'),
    ])

    let depositData = []
    let savingData = []

    try {
      depositData = parseProductData(await depositRes.json(), 'deposit')
    } catch (err) {
      console.error('❌ depositData 파싱 오류:', err)
      depositData = []
    }

    try {
      savingData = parseProductData(await savingRes.json(), 'saving')
    } catch (err) {
      console.error('❌ savingData 파싱 오류:', err)
      savingData = []
    }

    allItems.value.push(...depositData, ...savingData)
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
