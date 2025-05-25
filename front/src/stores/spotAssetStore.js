import axios from 'axios'
import { defineStore } from 'pinia'
import { computed, ref, watchEffect } from 'vue'

export const useSpotAssetStore = defineStore('spotAsset', () => {
  const spotAssetPrices = ref({})
  const selectedCommodity = ref('gold')
  const endDate = ref(new Date())
  const startDate = ref(new Date(new Date().setFullYear(new Date().getFullYear() - 1)))

  const commodityOptions = [
    { label: '금 가격 (USD)', value: 'gold' },
    { label: '은 가격 (USD)', value: 'silver' },
    { label: '원유 가격 (USD)', value: 'oil' },
    { label: '천연가스 가격 (USD)', value: 'gas' },
    { label: '옥수수 가격 (USD)', value: 'corn' },
    { label: '밀 가격 (USD)', value: 'wheat' },
    { label: '대두 가격 (USD)', value: 'soybean' },
    { label: '구리 가격 (USD)', value: 'copper' },
    { label: '백금 가격 (USD)', value: 'platinum' },
    { label: '팔라듐 가격 (USD)', value: 'palladium' },
  ]

  const fetchSpotAssetPrices = async (commodityName) => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/products/spotAssets/${commodityName}/`,
      )
      spotAssetPrices.value[commodityName] = response.data[commodityName]
    } catch (error) {
      console.error('Failed to fetch spot asset prices:', error)
    }
  }

  watchEffect(() => {
    if (selectedCommodity.value) {
      fetchSpotAssetPrices(selectedCommodity.value)
    }
  })

  const selectedData = computed(() => {
    if (
      !selectedCommodity.value ||
      !startDate.value ||
      !endDate.value ||
      !spotAssetPrices.value[selectedCommodity.value]
    ) {
      return []
    }

    return spotAssetPrices.value[selectedCommodity.value].filter((item) => {
      const date = new Date(item.date)
      return date >= new Date(startDate.value) && date <= new Date(endDate.value)
    })
  })

  return {
    spotAssetPrices,
    fetchSpotAssetPrices,
    selectedCommodity,
    startDate,
    endDate,
    commodityOptions,
    selectedData,
  }
})
