<template>
  <div class="profile-box">
    <div class="profile-left">
      <h3 class="section-title">Profile</h3>
      <img src="@/assets/profile.png" alt="profile" class="profile-image" />
      <div class="input-box">
        <label>이름</label>
        <input type="text" v-model="name" />
      </div>
      <div class="input-box">
        <label>이메일</label>
        <input type="email" v-model="email" />
      </div>
    </div>

    <div class="profile-right">
      <div><strong>닉네임</strong> <span>{{ nickname }}</span></div>
      <div><strong>연봉</strong> <span>**,***,***</span></div>
      <div class="invest-type">
        <strong>투자성향</strong>
        <div class="tags">
          <span class="tag">안정형</span>
          <span class="tag">안정 추구형</span>
          <span class="tag">위험 중립형</span>
          <span class="tag active">적극 투자형</span>
          <span class="tag">공격 투자형</span>
        </div>
      </div>
      <div>
        <strong>희망 투자 기간</strong>
        <!-- <img src="@/assets/chart-placeholder.png" alt="chart" class="chart-image" /> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('이지언')
const email = ref('example@ssafy.com')
const nickname = 'jiunchlrh'
</script>

<style scoped>
.profile-box {
	font-family: 'Pretendard', sans-serif;
  display: flex;
  background-color: white;
  width: 960px;
  height: 600px;
  border-radius: 30px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  padding: 40px;
  gap: 40px;
}

.section-title {
  color: #43B883;
  font-weight: bold;
  font-size: 18px;
  margin-bottom: 20px;
}

.profile-left {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.profile-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin-bottom: 20px;
}

.input-box {
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
  width: 100%;
}

.input-box label {
  margin-bottom: 5px;
  font-weight: 600;
}

.input-box input {
  padding: 8px;
  border-radius: 6px;
  border: 1px solid #ddd;
}

.profile-right {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 20px;
}

.invest-type .tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 6px;
}

.tag {
  background-color: #f0f0f0;
  padding: 4px 10px;
  border-radius: 16px;
  font-size: 13px;
  color: #333;
}

.tag.active {
  background-color: #43B883;
  color: white;
  font-weight: bold;
}

.chart-image {
  width: 100%;
  max-width: 320px;
  margin-top: 10px;
}
</style>
