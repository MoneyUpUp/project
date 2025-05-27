import { createRouter, createWebHistory } from 'vue-router'

// Layouts
import BaseLayout from '@/layouts/BaseLayout.vue'

// Views
import ArticleView from '@/views/ArticleView.vue'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import MapView from '@/views/MapView.vue'
import ProductView from '@/views/ProductView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchProductView from '@/views/SearchProductView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SpotAssetView from '@/views/SpotAssetView.vue'

// Components - Article
import ArticleComponent from '@/components/Article/ArticleComponent.vue'
import ArticleDetailUpdate from '@/components/Article/ArticleDetailUpdate.vue'
import ArticleDetail from '@/components/Article/ArticleDetailView.vue'
import CreateArticle from '@/components/Article/CreateArticle.vue'

// Components - Product
import depositList from '@/components/deposit/depositList.vue'
import savingView from '@/components/saving/savingView.vue'

// Components - Search
import SearchDetail from '@/components/search/SearchDetail.vue'
import searchList from '@/components/search/searchList.vue'

// Components - Profile
import AccessionProduct from '@/components/profile/AccessionProduct.vue'
import AiCustomPick from '@/components/profile/AiCustomPick.vue'
import profileUpdate from '@/components/profile/profileUpdate.vue'

// Components - Login
import KakaoLogin from '@/components/login/KakaoLogin.vue'
import logInComponent from '@/components/login/logInComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 로그인/회원가입 (네비 없음)
    {
      path: '/login',
      component: LoginView,
      redirect: '/login/main',
      children: [
        { path: 'main', name: 'login-main', component: logInComponent },
        { path: 'kakao', name: 'kakao', component: KakaoLogin },
      ],
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },

    // 공통 레이아웃 적용
    {
      path: '/',
      component: BaseLayout,
      children: [
        { path: '', name: 'home', component: HomeView },

        {
          path: 'article',
          name: 'article',
          component: ArticleView,
          children: [
            { path: '', name: 'articleList', component: ArticleComponent },
            { path: 'create', name: 'create', component: CreateArticle },
            { path: 'detail/:articleId', name: 'ArticleDetailView', component: ArticleDetail },
            {
              path: 'detail/:articleId/update',
              name: 'article-update',
              component: ArticleDetailUpdate,
            },
          ],
        },

        { path: 'map', name: 'map', component: MapView },
        { path: 'spotAsset', name: 'spotAsset', component: SpotAssetView },

        {
          path: 'product',
          name: 'product',
          component: ProductView,
          children: [
            { path: 'deposit', name: 'deposit', component: depositList },
            { path: 'saving', name: 'saving', component: savingView },
          ],
        },

        {
          path: 'profile',
          name: 'profile',
          component: ProfileView,
          children: [
            { path: '', redirect: { name: 'profile-update' } },
            { path: 'update', name: 'profile-update', component: profileUpdate },
            { path: 'accession', name: 'profile-accession', component: AccessionProduct },
            { path: 'aicustompick', name: 'profile-ai', component: AiCustomPick },
          ],
        },

        {
          path: 'searchproduct',
          name: 'searchproduct',
          component: SearchProductView,
          children: [
            { path: '', name: 'search-list', component: searchList },
            { path: 'detail/:id', name: 'search-detail', component: SearchDetail },
          ],
        },
      ],
    },
  ],
})

export default router
