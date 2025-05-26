import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000/community/'
  const articleList = ref(null)
  const router = useRouter()

  const getArticleList = async () => {
    try{
      const token = localStorage.getItem('token')
      const res = await axios.get(`${API_URL}articles/`, {
        headers: {
          Authorization: `Token ${token}`,
          'Content-Type': 'application/json',
        },
      })
      console.log('게시글 조회 성공')
      console.log(res.data)
      articleList.value = res.data
    } catch(err){
      console.log('게시글 조회 실패')
      console.log(err)
    }
  }

  const addArticle = async ({title, content, author}) => {
    try{
      const token = localStorage.getItem('token')
      const res = await axios.post(
        `${API_URL}articles/`,
        { title, content, author },
        {
          headers: {
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
          },
        },
      )
        console.log('게시글 생성 성공')
        console.log(res.data)
        getArticleList()
        router.push({ name: 'article' })

    }catch(err){
      console.log('게시글 생성 실패')
      console.log(err)
    }
  }
  return {
    articleList,
    getArticleList,
    addArticle,
  }
})
