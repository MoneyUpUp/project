import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useFavoriteStore = defineStore( 'favorit', () => {
    const API_URL = 'http://127.0.0.1:8000/accounts/'
    const favoriteList_deposits = ref([])

    const getFavoriteList = async () => {
        try {
            const token = localStorage.getItem('token')

            const res = await axios.get(
                `${API_URL}me/favorites/`,
                {
                    headers: { 
                        'Authorization': `Token ${token}`,
                        'Content-Type': 'application/json'
                    },
                },
            )
            console.log('찜목록 가져오기 성공')
            console.log(res.data)

            favoriteList_deposits.value = res.data.favorite_deposits || []
        }catch (err) {
            console.log('찜목록 가져오기 실패')
            console.log(err.response.data)
        }
    }

    const addFavorite = async (product) => {
      try {
        const token = localStorage.getItem('token')
        const res = await axios.post(
          `${API_URL}me/favorites/`,
          {
            type: product.type, // "deposit", "saving", "asset"
            id: product.id,
          },
          {
            headers: {
              Authorization: `Token ${token}`,
              'Content-Type': 'application/json',
            },
          },
        )
        console.log('찜 성공')
        console.log('✅ 찜 처리 결과:', res.data.message)
        // 찜 목록 다시 불러와서 최신화
        await getFavoriteList()
      } catch (err) {
        console.error('❌ 찜 처리 실패:', err.response?.data || err.message)
      }
    }
    
    return {
      favoriteList_deposits,
      getFavoriteList,
      addFavorite,
    }
})