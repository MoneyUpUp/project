<template>
    <div class="login-box">
      <div class="login-left">
          <form @submit.prevent="onlogin">
						<div class="login-right">
							<h4 style="text-align: center;">Login</h4>
							<label>Username</label>
							<input type="text" placeholder="Value" v-model="username"/>
							<label>Password</label>
							<input type="password" placeholder="Value" v-model="password" style="margin-bottom: 5%;"/>
							<button>Login</button>
						</div>
					</form>

					<h4>Social Login</h4>
					<div class="social">

							<div class="kakao" @click="kakaoLogin">
									<img src="@/assets/loginbutton/kakao.png" alt="">
							</div>
							<div class="google">
									<img src="@/assets/loginbutton/google.png" alt="">
							</div>
							<div class="naver">
									<img src="@/assets/loginbutton/naver.png" alt="">
							</div>
					</div>
      </div>
    </div>
  </template>
  
<script setup>
	import { ref } from 'vue'
	import { useRouter } from 'vue-router'
	import { useAccountStore } from '@/stores/accounts'
	const router = useRouter()
	const store = useAccountStore()
	const username = ref('')
	const password = ref('')

	const onlogin = () => {
		const userInfo = {
			username : username.value,
			password : password.value
		}
		store.logIn(userInfo)
	}

	const kakaoLogin = ( )=> {
		router.push({name:'kakao'})
	}
	
</script>
  
  <style scoped>
  .social {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 5%;
    margin-bottom: 5%;
  }
  .kakao{
    width: 50px;
    height: 50px;
    margin-right: 10%;
    background-color: #F9E500;
    border-radius: 10%;
    box-shadow:0 2px 6px rgba(0, 0, 0, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  .kakao img {
    width: 24px; /* 로고 크기 */
    height: 24px;
  }
  .google{
    width: 50px;
    height: 50px;
    margin-right: 10%;
    background-color: #ffffff;
    border-radius: 10%;
    box-shadow:0 2px 6px rgba(0, 0, 0, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .google img {
    width: 30px; /* 로고 크기 */
    height: 30px;
  }
  .naver{
    width: 50px;
    height: 50px;
    background-color: #03D166;
    border-radius: 10%;
    box-shadow:0 2px 6px rgba(0, 0, 0, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .naver img {
    width: 24px; /* 로고 크기 */
    height: 24px;
  }

  form {
    width: 395px;
    margin: 0;
    padding-top: 3%;
    padding-right: 3%;
    border: none;
    background: none;
  }

  h4{
    font-family: 'Pretendard', sans-serif;
    color:#43B883;
    padding-top: 15% ;
    text-align: center;
  }


  
  .login-box {
    display: flex;
    background-color: white;
    width: 500px;
    height: 600px;
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
    background-color: #43B883;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 6px;
    cursor: pointer;
  }
  
  .green {
    color: #43B883;
  }
  
  .bold-green {
    font-weight: 800;
    color: #43B883;
  }
  </style>
  