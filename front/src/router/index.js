import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import LoginView from '@/views/LoginView.vue'
import ProductView from '@/views/ProductView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SignUpView from '@/views/SignUpView.vue'
import MapView from '@/views/MapView.vue'
import SpotAssetView from '@/views/SpotAssetView.vue'
import searchProductView from '@/views/searchProductView.vue'

import depositList from '@/components/deposit/depositList.vue'
import savingView from '@/components/saving/savingView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
        {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/spotAsset',
      name: 'spotAsset',
      component: SpotAssetView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView,
      children: [{
        path: 'deposit',
        name: 'deposit',
        component:depositList
      },
      {
        path: 'saving',
        name: 'saving',
        component: savingView
      }]
    },
    {
      path: '/profile/',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/searchproduct',
      name: 'searchproduct',
      component: searchProductView
    }
  ],
})

export default router
