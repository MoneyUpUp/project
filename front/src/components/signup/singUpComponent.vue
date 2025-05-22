<template>
  <div class="signup-box">
    <div class="signup-left">
      <img src="@/assets/signup.png" alt="signup mascot" class="signup-image" />
    </div>
    <div class="signup-right">
      <label>Name</label>
      <input type="text" placeholder="Value" />
      <label>Email</label>
      <input type="email" placeholder="Value" />
      <label>Password</label>
      <input type="password" placeholder="Value" />
      <label>Age</label>
      <input type="number" placeholder="Value" />
      <button>Sign in</button>
    </div>
  </div>
</template>

<script setup>
// props나 emits 필요 시 여기 추가
</script>

<style scoped>
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
