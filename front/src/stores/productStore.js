// stores/productStore.js
import { BANKS_BY_ID, BANK_OPTIONS, getBankLogoById } from '@/constants/banks'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useProductStore = defineStore('product', () => {
  const selectedBank = ref('all') // 은행 ID를 저장
  const selectedIndex = ref(0)
  const selectedTypes = ref(['deposit', 'saving'])
  const allItems = ref([])

  // 🔹 은행명 필터 (은행 ID 기반으로 비교)
  const matchesBank = (item) => {
    return selectedBank.value === 'all' || item.bank.fin_co_no === selectedBank.value
  }

  // 🔹 상품유형 필터
  const matchesType = (item) => {
    return selectedTypes.value.includes(item.type)
  }

  // 🔹 기간 필터
  const matchesPeriod = (item) => {
    return selectedIndex.value === 0 || item.save_trm === selectedIndex.value * 6
  }

  // 🔹 최종 필터링
  const filteredItems = computed(() =>
    allItems.value.filter((item) => matchesType(item) && matchesBank(item) && matchesPeriod(item)),
  )

  const bankOptions = computed(() => BANK_OPTIONS)

  async function depositData() {
    const res = await fetch('/deposit.json')
    const data = await res.json()

    data.forEach((product) => {
      product.type = 'deposit'
      const matched = BANKS_BY_ID[product.bank.fin_co_no]
      if (matched) {
        product.bank.logo = getBankLogoById(product.bank.fin_co_no)
        product.bank.kor_co_nm = matched.name
      }
    })

    allItems.value.push(...data)
  }

  async function savingData() {
    const res = await fetch('/saving.json')
    const data = await res.json()

    data.forEach((product) => {
      product.type = 'saving'
      const matched = BANKS_BY_ID[product.bank.fin_co_no]
      if (matched) {
        product.bank.logo = getBankLogoById(product.bank.fin_co_no)
        product.bank.kor_co_nm = matched.name
      }
    })

    allItems.value.push(...data)
  }

  async function fetchAllProducts() {
    allItems.value = []
    await Promise.all([depositData(), savingData()])
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
