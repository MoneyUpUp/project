import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const API_URL = "http://127.0.0.1:8000/";
    const createUser = ({username, email, password}) => {
        axios({
            method: 'post',
            url: `${API_URL}dj-rest-auth/signup/`,
            data: {
                username, email, password
            }
        })
        .then(res => {
            console.log('회원가입 성공!')
            console.log(res.data)
        })
        .catch(err => console.log(err))
    }
  return { 
    createUser
  }
})
