<template>
  <div class="login-box">
    <div class="login-left">
      <form @submit.prevent="onlogin">
        <div class="login-right">
          <h4 style="text-align: center">Money Up</h4>
          <label>이메일</label>
          <input
            type="text"
            placeholder="이메일을 입력 해 주세요."
            v-model="email"
          />
          <label>비밀번호</label>
          <input
            type="password"
            placeholder="비밀번호를 입력 해 주세요."
            v-model="password"
            style="margin-bottom: 5%"
          />
          <button>로그인</button>
        </div>
      </form>
      <RouterLink :to="{ name: 'signup' }">회원가입하러 가기</RouterLink>
      <h4>Social Login</h4>
      <div class="social">
        <div
          class="kakao"
          @click="kakaoLogin"
        >
          <img
            src="@/assets/loginbutton/kakao.png"
            alt=""
          />
        </div>
        <div class="google">
          <img
            src="@/assets/loginbutton/google.png"
            alt=""
          />
        </div>
        <div class="naver">
          <img
            src="@/assets/loginbutton/naver.png"
            alt=""
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useAccountStore()
const email = ref('')
const password = ref('')

const onlogin = async () => {
  const userInfo = {
    email: email.value,
    password: password.value,
  }
  const success = await store.logIn(userInfo)

  if (success) {
    router.push({ name: 'home' })
  } else {
    alert('로그인에 실패했습니다. 아이디나 비밀번호를 확인하세요.')
    // 또는 에러 메시지 ref에 담아서 화면에 띄워도 됩니다
  }
}

const kakaoLogin = () => {
  router.push({ name: 'kakao' })
}
</script>

<style scoped>
.social {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 5%;
  /* margin-bottom: 15%; */ /* 이전 여백 조정 제거 */
  padding-bottom: 15%; /* 아이콘 아래에 패딩 추가 */
}
.kakao,
.google,
.naver {
  /* 공통 스타일 */
  width: 50px;
  height: 50px;
  min-width: 50px; /* 최소 너비 설정 */
  min-height: 50px; /* 최소 높이 설정 */
  border-radius: 10%;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin-right: 10%;
}

.kakao {
  background-color: #f9e500;
}
.google {
  background-color: #ffffff;
}
.naver {
  background-color: #03d166;
  margin-right: 0; /* 마지막 요소 오른쪽 마진 제거 */
}

.kakao img {
  width: 24px;
  height: 24px;
  object-fit: contain;
}
.google img {
  width: 30px;
  height: 30px;
  object-fit: contain;
}
.naver img {
  width: 24px;
  height: 24px;
  object-fit: contain; /* 네이버 아이콘에도 object-fit 추가 */
}

form {
  width: 395px;
  margin: 0;
  padding-top: 3%;
  padding-right: 3%;
  border: none;
  background: none;
}

h4 {
  font-family: 'Pretendard', sans-serif;
  color: #43b883;
  padding-top: 15%;
  text-align: center;
}

.login-box {
  display: flex;
  background-color: white;
  width: 500px;
  height: 650px; /* 높이를 600px에서 650px로 늘림 */
  border-radius: 30px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  padding: 40px;
  gap: 40px;
}

.login-left {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* justify-content: center; */
}

.login-image {
  width: 388px;
  height: 491px;
  margin-top: 20px;
}

.login-right {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
  justify-content: center;
}

.login-right input {
  padding: 8px 12px;
  border-radius: 6px;
  border: 1px solid #ddd;
  outline: none;
}

.login-right button {
  margin-top: 8px;
  background-color: #43b883;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 6px;
  cursor: pointer;
}

.green {
  color: #43b883;
}

.bold-green {
  font-weight: 800;
  color: #43b883;
}
</style>
