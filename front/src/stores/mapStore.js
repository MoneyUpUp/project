// stores/mapStore.js
import { searchPlace } from '@/utils/map/mapHandler'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useMapStore = defineStore('map', () => {
  const selectedState = ref('')
  const selectedCity = ref('')
  const selectedBank = ref('')

  const data = ref(null)
  const map = ref(null)
  const myLocation = ref(null)
  const searchResults = ref([])

  const states = computed(() => data.value?.mapInfo.map((e) => e.name) || [])
  const cities = computed(() => {
    const region = data.value?.mapInfo.find((e) => e.name === selectedState.value)
    return region ? region.countries : []
  })
  const banks = computed(() => data.value?.bankInfo || [])

  const onStateChange = () => {
    selectedCity.value = ''
  }

  const onSearch = () => {
    const keyword = `${selectedState.value} ${selectedCity.value} ${selectedBank.value}`
    console.log('[검색 키워드]', keyword)
    console.log('[내 위치]', myLocation.value)
    console.log('[지도 객체]', map.value)

    if (!myLocation.value) {
      alert('위치 정보를 사용할 수 없습니다.')
      return
    }

    searchPlace(map.value, keyword, myLocation.value, (results) => {
      searchResults.value = results
      if (results.length === 0) alert('검색 결과가 없습니다.')
    })
  }

  const setMyLocationOnce = (lat, lng) => {
    if (!myLocation.value) {
      myLocation.value = new kakao.maps.LatLng(lat, lng)
    }
  }

  return {
    selectedState,
    selectedCity,
    selectedBank,
    data,
    map,
    myLocation,
    searchResults,
    states,
    cities,
    banks,
    onSearch,
    onStateChange,
    setMyLocationOnce,
  }
})
