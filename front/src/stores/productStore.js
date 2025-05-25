import { BANK_OPTIONS } from '@/constants/banks'
import { matchesBank, matchesPeriod, parseProductData } from '@/utils/product/productFilters'
import axios from 'axios'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useProductStore = defineStore('product', () => {
  const selectedBank = ref('all')
  const selectedIndex = ref(0)
  const selectedTypes = ref('all') // "all", "deposit", "saving"
  const sortOption = ref('name')
  const allItems = ref([])

  const advancedFilters = ref({
    internet: false,
    smartphone: false,
    telephone: false,
    branch: false,
  })

  const selectedTerm = ref(null) // null means no filter; values are 6, 12, 24, 36

  const bankOptions = computed(() => BANK_OPTIONS)

  function getMaxRate(product) {
    return Math.max(...(product.options || []).map((opt) => parseFloat(opt.intr_rate2) || 0))
  }

  function getBaseRate(product) {
    const sorted = [...(product.options || [])].sort((a, b) => a.save_trm - b.save_trm)
    return parseFloat(sorted[0]?.intr_rate) || 0
  }

  const filteredItems = computed(() => {
    const filtered = allItems.value.filter((item) => {
      if (selectedTypes.value !== 'all' && item.type !== selectedTypes.value) return false
      if (!matchesBank(item, selectedBank.value)) return false
      if (!matchesPeriod(item, selectedIndex.value)) return false

      const joinWayList = Array.isArray(item.join_way)
        ? item.join_way
        : typeof item.join_way === 'string'
          ? item.join_way.split(',').map((s) => s.trim())
          : []

      if (
        (advancedFilters.value.internet && !joinWayList.includes('인터넷')) ||
        (advancedFilters.value.smartphone && !joinWayList.includes('스마트폰')) ||
        (advancedFilters.value.telephone && !joinWayList.some((way) => way.includes('전화'))) ||
        (advancedFilters.value.branch && !joinWayList.includes('영업점'))
      )
        return false

      if (
        selectedTerm.value &&
        !item.options.some((opt) => Number(opt.save_trm) === selectedTerm.value)
      )
        return false

      return true
    })

    return filtered.sort((a, b) => {
      if (sortOption.value === 'rate_max') {
        return getMaxRate(b) - getMaxRate(a)
      } else if (sortOption.value === 'rate_base') {
        return getBaseRate(b) - getBaseRate(a)
      } else {
        return a.fin_prdt_nm.localeCompare(b.fin_prdt_nm)
      }
    })
  })

  async function fetchAllProducts() {
    allItems.value = []

    try {
      const token = localStorage.getItem('token') // 또는 sessionStorage 등에서 가져오기

      const res = await axios.get('http://127.0.0.1:8000/products/', {
        headers: {
          Authorization: `Token ${token}`,
        },
      })

      const data = res.data
      const depositData = parseProductData(data.deposit_products || [], 'deposit')
      const savingData = parseProductData(data.saving_products || [], 'saving')

      allItems.value.push(...depositData, ...savingData)
    } catch (err) {
      console.error('❌ 상품 데이터 요청 실패:', err)
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
    advancedFilters,
    selectedTerm,
  }
})
