
import { createPinia } from 'pinia';
import { createApp } from 'vue';

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue';
import router from './router';

import '@/assets/styles/main.scss';

const app = createApp(App)
const key = import.meta.env.VITE_KAKAO_API_JS_KEY
const pinia = createPinia()

app.use(createPinia())
app.use(router)
app.component('VueDatePicker', VueDatePicker);
pinia.use(piniaPluginPersistedstate)

app.mount('#app')

window.Kakao.init(key)