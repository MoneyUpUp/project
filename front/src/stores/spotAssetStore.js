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
      console.log(`Fetching data for: ${commodityName}`);
      const response = await axios.get(
        `http://127.0.0.1:8000/products/spotAssets/${commodityName}/`,
      );
      console.log(`Full response data for ${commodityName}:`, response.data); // 전체 응답 데이터 로깅

      // 응답 구조에 따라 분기
      if (Array.isArray(response.data)) {
        spotAssetPrices.value[commodityName] = response.data;
      } else if (response.data && response.data[commodityName]) {
        spotAssetPrices.value[commodityName] = response.data[commodityName];
      } else {
        console.warn(`Unexpected data structure for ${commodityName}:`, response.data);
        spotAssetPrices.value[commodityName] = []; // 데이터가 없거나 예상과 다르면 빈 배열로 초기화
      }

      if (spotAssetPrices.value[commodityName] && spotAssetPrices.value[commodityName].length > 0) {
        // console.log(`First item for ${commodityName}:`, spotAssetPrices.value[commodityName][0]); // 디버깅 로그 제거
        // console.log(`Last item for ${commodityName}:`, spotAssetPrices.value[commodityName][spotAssetPrices.value[commodityName].length - 1]); // 디버깅 로그 제거
        // console.log(`Keys and values of first item for ${commodityName}:`); // 디버깅 로그 제거
        // for (const key in spotAssetPrices.value[commodityName][0]) { // 디버깅 로그 제거
        //   console.log(`  ${key}:`, spotAssetPrices.value[commodityName][0][key]); // 디버깅 로그 제거
        // }
      }
    } catch (error) {
      console.error('Failed to fetch spot asset prices:', error);
      spotAssetPrices.value[commodityName] = []; // 에러 발생 시 빈 배열로 초기화
    }
  };

  watchEffect(() => {
    if (selectedCommodity.value) {
      fetchSpotAssetPrices(selectedCommodity.value);
    }
  });

  const selectedData = computed(() => {
    // console.log('Calculating selectedData...'); // 디버깅 로그 제거
    // console.log('selectedCommodity:', selectedCommodity.value); // 디버깅 로그 제거
    // console.log('startDate:', startDate.value); // 디버깅 로그 제거
    // console.log('endDate:', endDate.value); // 디버깅 로그 제거
    // console.log('spotAssetPrices[selectedCommodity]:', spotAssetPrices.value[selectedCommodity.value]); // 디버깅 로그 제거

    if (
      !selectedCommodity.value ||
      !startDate.value ||
      !endDate.value ||
      !spotAssetPrices.value[selectedCommodity.value]
    ) {
      // console.log('Selected data is empty due to missing parameters or data.'); // 디버깅 로그 제거
      return [];
    }

    const filteredData = spotAssetPrices.value[selectedCommodity.value].filter((item) => {
      const date = new Date(item.date);
      const start = new Date(startDate.value);
      start.setHours(0, 0, 0, 0); // 시작일의 시간을 00:00:00으로 설정
      const end = new Date(endDate.value);
      end.setHours(23, 59, 59, 999); // 종료일의 시간을 23:59:59으로 설정

      const isWithinRange = date >= start && date <= end;
      // console.log(`Item date: ${item.date}, Start: ${start.toISOString()}, End: ${end.toISOString()}, Within range: ${isWithinRange}`);
      return isWithinRange;
    });
    console.log('Filtered data:', filteredData);
    return filteredData;
  });

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
