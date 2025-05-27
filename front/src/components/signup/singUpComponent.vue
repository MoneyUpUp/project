<template>
  <div class="signup-box">
    <div class="signup-left">
      <img
        src="@/assets/signup.png"
        alt="signup mascot"
        class="signup-image"
      />
    </div>
    <form @submit.prevent="onSignup">
      <div class="signup-right">
        <label>이름</label>
        <input
          type="text"
          placeholder="이름을 입력해주세요."
          v-model="name"
        />
        <label>이메일</label>
        <input
          type="email"
          placeholder="이메일을 입력해주세요."
          v-model="email"
        />
        <label>비밀번호</label>
        <input
          type="password"
          placeholder="비밀번호을 입력해주세요."
          v-model="password"
        />
        <label>나이</label>
        <input
          type="number"
          placeholder="나이를 입력해주세요."
          v-model="age"
        />
        <button>회원가입</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'
import { ref } from 'vue'

const name = ref('')
const email = ref('')
const password = ref('')
const age = ref(0)

const store = useAccountStore()
const onSignup = function () {
  const userInfo = {
    name: name.value,
    email: email.value,
    password: password.value,
    age: age.value,
  }

  store.createUser(userInfo)
}
</script>

<style scoped>
form {
  width: 395px;
  margin: 0;
  padding-top: 3%;
  padding-right: 3%;
  border: none;
  background: none;
}

.signup-box {
  display: flex;
  background-color: white;
  width: 960px;
  height: 600px;
  border-radius: 30px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  padding: 40px;
  gap: 40px;
}

.signup-left {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.signup-image {
  width: 388px;
  height: 491px;
  margin-top: 20px;
}

.signup-right {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
  justify-content: center;
}

.signup-right input {
  padding: 8px 12px;
  border-radius: 6px;
  border: 1px solid #ddd;
  outline: none;
}

.signup-right button {
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
