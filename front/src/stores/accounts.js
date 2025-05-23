import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
  const API_URL = "http://127.0.0.1:8000/";
  const token = ref('')
  const router = useRouter()
    const createUser = ({username, email, password, age}) => {
        axios({
            method: 'post',
            url: `${API_URL}auth/signup/`,
            data: {
                username:username,
                email:email, 
                password1: password,
                password2: password,
                age:age
            },
            headers: {
              'Content-Type': 'application/json'
            }
        })
        .then(res => {
            console.log('회원가입 성공!')
            console.log(res.data)
            token.value = res.data.key
            router.push({name:'login'})
            
        })
        .catch(err => console.log(err))
    }
  return { 
    createUser
  }
})
