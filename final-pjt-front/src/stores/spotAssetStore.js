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

      // 응답 구조에 따라 분기
      if (Array.isArray(response.data)) {
        spotAssetPrices.value[commodityName] = response.data
      } else if (response.data && response.data[commodityName]) {
        spotAssetPrices.value[commodityName] = response.data[commodityName]
      } else {
        spotAssetPrices.value[commodityName] = [] // 데이터가 없거나 예상과 다르면 빈 배열로 초기화
      }

      if (spotAssetPrices.value[commodityName] && spotAssetPrices.value[commodityName].length > 0) {
      }
    } catch (error) {
      spotAssetPrices.value[commodityName] = [] // 에러 발생 시 빈 배열로 초기화
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

    const filteredData = spotAssetPrices.value[selectedCommodity.value].filter((item) => {
      const date = new Date(item.date)
      const start = new Date(startDate.value)
      start.setHours(0, 0, 0, 0) // 시작일의 시간을 00:00:00으로 설정
      const end = new Date(endDate.value)
      end.setHours(23, 59, 59, 999) // 종료일의 시간을 23:59:59으로 설정

      const isWithinRange = date >= start && date <= end
      return isWithinRange
    })
    return filteredData
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
