<template>
  <div>
    <nav class="navbar">
      <div class="left-section">
        <RouterLink to="/" class="logo-link">
          <div class="logo">MoneyUp</div>
        </RouterLink>

        <ul class="nav-links">
          <li>
            <RouterLink to="/product">상품</RouterLink>
          </li>
          <li>
            <RouterLink to="/spotAsset">현물</RouterLink>
          </li>
          <li>
            <RouterLink to="/map">지도</RouterLink>
          </li>
          <li>
            <RouterLink to="/article">커뮤니티</RouterLink>
          </li>
          <li>
            <RouterLink to="/searchproduct">관심종목검색</RouterLink>
          </li>
        </ul>
      </div>

      <div class="right-section">
        <button class="login-btn">
          <RouterLink to="/login" class="signup-btn-link">로그인</RouterLink>
        </button>
        <button class="signup-btn">
          <RouterLink to="/signup" class="signup-btn-link">가입하기</RouterLink>
        </button>
      </div>
    </nav>

    <RouterView />
  </div>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>



<style scoped>
.login-btn{
  background-color: #43B883;
  color: #fff;
  font-weight: 300;
  font-size: 14px;
  padding: 8px 16px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.login-btn-link {
  text-decoration: none;
  /* 밑줄 제거 */
  color: white;
}

.login-btn:hover {
  background-color: #369f6d;
}

.right-section {
  display: flex;
  gap: 12px; /* 버튼 간격 추가 */
  align-items: center;
}

.navbar {
  width: 100%;
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 350px;
  background-color: white;
  border-bottom: 1px solid #e0e0e0;
  font-family: 'Pretendard', sans-serif;
}

.wrapper {
  max-width: 1200px;
  padding: 0 24px;
  /* 모바일에선 좌우 여백 확보 */
  height: 60px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.left-section {
  display: flex;
  align-items: center;
  gap: 40px;
  /* 로고와 메뉴 사이 간격 */
}

.logo {
  font-family: 'Pretendard', sans-serif;
  font-weight: 900;
  font-size: 24px;
  line-height: 36px;
  letter-spacing: 0;
  color: #43B883;
}

.logo-link {
  text-decoration: none;
  /* 밑줄 제거 */
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 24px;
  margin: 0;
  padding: 0;
}

.nav-links li {
  cursor: pointer;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  color: #43B883;
}

.nav-links a {
  text-decoration: none;
  color: inherit;
}

.signup-btn {
  background-color: #43B883;
  color: white;
  font-weight: 300;
  font-size: 14px;
  padding: 8px 16px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.signup-btn-link {
  text-decoration: none;
  /* 밑줄 제거 */
  color: white;
}

.signup-btn:hover {
  background-color: #369f6d;
}
</style>