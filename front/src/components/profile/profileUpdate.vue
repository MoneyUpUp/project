<template>
  <div class="container-lg">
    <div class="custom-container">
      <div style="margin: 10% auto;">
        <img src="@/assets/profile.png">
      </div>

      <div style="margin: 10% auto;">
        <p class="name">{{ store.userInfo.username }}</p>

        <div class="info-update">
          <span class="info">닉네임</span>
          <UpdateInputBar
            :user="store.userInfo.nickname"
          />
        </div>

        <div class="info-update">
          <span class="info">이메일</span>
          <UpdateInputBar
            :user="store.userInfo.email"
          />
        </div>
        
        <div class="info-update">
          <span class="info">나이</span>
          <UpdateInputBar
            :user="store.userInfo.age"
          />
        </div>
      </div>
    </div>
    <hr style="color: #adb5bd;">
    <p class="fontStyle">금융 프로필 정보</p> 
    <div class="custom-container2">
      <div>
        <div class="custom-container3">
          <p class="fontStyle" style="margin-right: 40px;">연봉</p> 
          <SalaryInputBar/>
        </div>
        <p class="fontStyle" style="margin-right: 40px; margin-top: 66px;">투자성향</p> 
        <PropensityBtn/>
        <p class="fontStyle" style="margin-right: 40px; margin-top: 66px;">희망투자기간</p> 
      </div>
    </div> 
  </div>
</template>

<script setup>
import UpdateInputBar from '../button/UpdateInputBar.vue';
import SalaryInputBar from '../button/SalaryInputBar.vue';
import PropensityBtn from '../button/PropensityBtn.vue';
import { useAccountStore } from '@/stores/accounts';
import { onMounted } from 'vue';

const store = useAccountStore();

onMounted(async () => {
  await store.getUserInfo();
});




</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

img {
    width: 100%;
    max-width: 300px;    // ✅ 최대 너비 지정
    height: auto;        // ✅ 비율 자동 유지
    border-radius: 50%;  // 프로필 원형 이미지일 경우
    display: block;
  }

.custom-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 5%;
  gap: 40px;

  @media (max-width: 1140px) {
    flex-direction: column;
    align-items: center;
  }
}

.custom-container2 {
  display: flex;  
  justify-content: flex-end;
  width: 100%;         // ✅ 반응형으로 기본 100% 차지
}

.custom-container3 {
  display: flex; 
  margin-right: 40px; 
}

.name {
  font-family: $font-base;
  font-size: 32px;
  font-weight: 700;
}

.fontStyle {
  font-family: $font-base;
  font-size: $font-size-lg;
  font-weight: 500;
}

.info {
  width:96px;
  font-weight: 700;
  padding-top: 10px;
  padding-bottom: 60px;

}

.info-update {
  display: flex;
}


</style>