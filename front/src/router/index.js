import { createRouter, createWebHistory } from 'vue-router'

import BaseLayout from '@/layouts/BaseLayout.vue'

import ArticleView from '@/views/ArticleView.vue'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import MapView from '@/views/MapView.vue'
import ProductView from '@/views/ProductView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchProductView from '@/views/SearchProductView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SpotAssetView from '@/views/SpotAssetView.vue'

import depositList from '@/components/deposit/depositList.vue'
import savingView from '@/components/saving/savingView.vue'

import ArticleComponent from '@/components/Article/ArticleComponent.vue'
import ArticleDetail from '@/components/Article/ArticleDetail.vue'
import CreateArticle from '@/components/Article/CreateArticle.vue'

import searchList from '@/components/search/searchList.vue'
import SearchDetail from '@/components/search/SearchDetail.vue'

import profileUpdate from '@/components/profile/profileUpdate.vue'
import AccessionProduct from '@/components/profile/AccessionProduct.vue'
import AiCustomPick from '@/components/profile/AiCustomPick.vue'

import logInComponent from '@/components/login/logInComponent.vue'
import KakaoLogin from '@/components/login/KakaoLogin.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: BaseLayout, // ✅ 공통 레이아웃
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView,
        },
        {
          path: 'article',
          name: 'article',
          component: ArticleView,
          children: [
            {
              path: '',
              name: '',
              component: ArticleComponent,
            },
            {
              path: 'create',
              name: 'create',
              component: CreateArticle,
            },
            {
              path: 'detail',
              name: 'article-detail',
              component: ArticleDetail,
            },
          ],
        },
        {
          path: 'map',
          name: 'map',
          component: MapView,
        },
        {
          path: 'spotAsset',
          name: 'spotAsset',
          component: SpotAssetView,
        },
        {
          path: 'product',
          name: 'product',
          component: ProductView,
          children: [
            {
              path: 'deposit',
              name: 'deposit',
              component: depositList,
            },
            {
              path: 'saving',
              name: 'saving',
              component: savingView,
            },
          ],
        },
        {
          path: 'profile',
          name: 'profile',
          component: ProfileView,
          children: [
            {
              path: '',
              redirect: { name: 'profile-update' }, // 자동 리디렉트
            },
            {
              path: 'update',
              name: 'profile-update',
              component: profileUpdate,
            },
            {
              path: 'accession',
              name: 'profile-accession',
              component: AccessionProduct,
            },
            {
              path: 'aicustompick',
              name: 'profile-ai',
              component: AiCustomPick,
            },
          ],
        },
        {
          path: 'searchproduct',
          name: 'searchproduct',
          component: SearchProductView,
          children: [
            {
              path: '',
              name: '',
              component: searchList,
            },
            {
              path: 'detail/:id',
              name: 'search-detail',
              component: SearchDetail,
            },
          ],
        },
      ],
    },
    // ✅ 로그인/회원가입은 네비 없는 독립 페이지
    {
      path: '/login',
      component: LoginView,
      redirect: '/login/main',
      children: [
        {
          path: 'main',
          name: 'login-main',
          component: logInComponent,
        },
        {
          path: 'kakao',
          name: 'kakao',
          component: KakaoLogin,
        },
      ],
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
  ],
})

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView,
//     },
//     {
//       path: '/article',
//       name: 'article',
//       component: ArticleView,
//     },
//     {
//       path: '/map',
//       name: 'map',
//       component: MapView,
//     },
//     {
//       path: '/spotAsset',
//       name: 'spotAsset',
//       component: SpotAssetView,
//     },
//     {
//       path: '/login',
//       name: 'login',
//       component: LoginView,
//     },
//     {
//       path: '/product',
//       name: 'product',
//       component: ProductView,
//       children: [
//         {
//           path: 'deposit',
//           name: 'deposit',
//           component: depositList,
//         },
//         {
//           path: 'saving',
//           name: 'saving',
//           component: savingView,
//         },
//       ],
//     },
//     {
//       path: '/profile/',
//       name: 'profile',
//       component: ProfileView,
//     },
//     {
//       path: '/signup',
//       name: 'signup',
//       component: SignUpView,
//     },
//     {
//       path: '/searchproduct',
//       name: 'searchproduct',
//       component: SearchProductView,
//     },
//   ],
// })

export default router
