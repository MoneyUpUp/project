import { createPinia } from 'pinia'
import { createApp } from 'vue'

import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

import '@/assets/styles/main.scss'

const app = createApp(App)
const pinia = createPinia() // Pinia 인스턴스 생성

pinia.use(piniaPluginPersistedstate) // 생성된 인스턴스에 플러그인 등록

app.use(pinia) // 앱에 해당 Pinia 인스턴스 사용
app.use(router)
app.component('VueDatePicker', VueDatePicker)

app.mount('#app')
