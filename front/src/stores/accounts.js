import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'

export const useAccountStore = defineStore(
  'account',
  () => {
    const API_URL = 'http://127.0.0.1:8000/'
    const initialTokenFromLocalStorage = localStorage.getItem('token');
    const token = ref(initialTokenFromLocalStorage || '');
    const userInfo = ref({})
    const propensity = ref('')
    const period = ref('')

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
          token.value = res.data.toekn
          localStorage.setItem('token', res.data.toekn)
          router.push({ name: 'home' })
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

        token.value = res.data.toekn
        localStorage.setItem('token', res.data.toekn)
        return true
      } catch (err) {
        console.log('로그인 실패:', err.response?.data || err.message)
        return false
      }
    }
    const isLogin = computed(() => {
      return token.value.length >= 1;
    })

    const logOut = () => {
      token.value = ''
      localStorage.removeItem('token')
      router.push({ name: 'home' })
    }

    const setToken = (value) => {
      token.value = value;
    }

    const getUserInfo = async (info) => {
      try {
        const res = await axios.get(
          `${API_URL}accounts/me/`,
          {
            headers: { 'Authorization': `Token ${token.value}` },
          },
        )
        console.log('유저정보 가져오기 성공');
        console.log(res.data)
        localStorage.setItem('username', res.data.nickname)
        userInfo.value = res.data
      } catch (err) {
        console.log('유저 정보 불러오기 실패:', err.response?.data || err.message)
      }
    }

    const updateUserInfo = async ({nickname, age, email, annual_income}) => {
      try {
        const res = await axios.patch(
          `${API_URL}accounts/me/`,
          {
            nickname, age, email, annual_income
          },
          {
            headers: { 'Authorization': `Token ${token.value}` },
          },
        )
        console.log('유저 정보 수정 성공');
        console.log(res.data)
        getUserInfo(res.data)
      } catch (err) {
        console.log('유저 정보 수정 실패:', err.response?.data || err.message)
      }
    }

    const setPropensity = (value) => {
      propensity.value = value
    }

    const setPeriod = (value) => {
      period.value = value
    }

    return {
      createUser,
      logIn,
      isLogin,
      token,
      logOut,
      setToken,
      getUserInfo,
      userInfo,
      updateUserInfo,
      propensity,
      setPropensity,
      setPeriod
    }
  },
  { persist: true }, // Temporarily disabled for debugging
)
