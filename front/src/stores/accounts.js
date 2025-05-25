import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'

export const useAccountStore = defineStore(
  'account',
  () => {
    const API_URL = 'http://127.0.0.1:8000/'
    const token = ref(localStorage.getItem('token') || '')
    const router = useRouter()
    const createUser = ({ username, email, password, age }) => {
      axios({
        method: 'post',
        url: `${API_URL}auth/signup/`,
        data: {
          username: username,
          email: email,
          password1: password,
          password2: password,
          nickname: username,
          age: age,
        },
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((res) => {
          console.log('회원가입 성공!')
          console.log(res.data)
          router.push({ name: 'login' })
        })
        .catch((err) => console.log(err))
    }

    const logIn = async ({ username, password }) => {
      try {
        const res = await axios.post(
          `${API_URL}auth/login/`,
          {
            username,
            password,
          },
          {
            headers: { 'Content-Type': 'application/json' },
          },
        )

        token.value = res.data.key
        localStorage.setItem('token', res.data.key)
        return true
      } catch (err) {
        console.log('로그인 실패:', err.response?.data || err.message)
        return false
      }
    }
    const isLogin = computed(() => token.value.length >= 1)

    const logOut = () => {
      token.value = ''
      localStorage.removeItem('token')
      router.push({ name: 'home' })
    }

    return {
      createUser,
      logIn,
      isLogin,
      token,
      logOut,
    }
  },
  { persist: true },
)
