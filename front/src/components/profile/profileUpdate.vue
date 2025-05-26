<template>
  <div class="container-lg">
    <div class="custom-container">
      <div style="margin: 50px 50px;">
        <img src="@/assets/profile.png">
      </div>
      <form @submit.prevent="onSubmit">
        <div style="margin: 10% auto;">
          <p class="name">{{ store.userInfo.nickname }}</p>

          <div class="info-update">
            <span class="info" id="nickname">닉네임</span>
            <UpdateInputBar
              :user="store.userInfo.nickname"
            />
          </div>

          <div class="info-update">
            <span class="info" id="email">이메일</span>
            <UpdateInputBar
              :user="store.userInfo.email"
            />
          </div>
          
          <div class="info-update">
            <span class="info" id="age">나이</span>
            <UpdateInputBar
              :user="store.userInfo.age"
            />
          </div>
          <div class="update-button-container">
            <UpdateButton/>
          </div>

        </div>
      </form>
    </div>
    <hr style="color: #adb5bd;">
    <p class="fontStyle">금융 프로필 정보</p> 
    <div class="custom-container2">
      <div>
        <div class="custom-container3">
          <form @submit.prevent="onSubmit2">
            <p class="fontStyle pTag" style="margin-bottom: 40px; margin-left: -50px;" id="annual_income">연봉</p> 
            <SalaryInputBar
              :user="store.userInfo.annual_income"
            />
          </form>
        </div>
        <p class="fontStyle pTag" style="margin-right: 40px; margin-top: 66px;">투자성향</p> 
        <PropensityBtn/>
        <p class="fontStyle pTag" style="margin-right: 40px; margin-top: 66px;">희망투자기간</p> 
        <!-- 희망투자기간 컴포넌트가 필요하다면 여기에 추가 -->
         <PeriodBtn/>
         <div style="height: 100px;"></div>
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
import UpdateButton from '../button/UpdateButton.vue';
import PeriodBtn from '../button/PeriodBtn.vue';

const store = useAccountStore();

onMounted(async () => {
  await store.getUserInfo();
});

const onSubmit = (e) => {
  const updatedData = {};
  
  const updateGroups = e.target.querySelectorAll('.info-update');

  updateGroups.forEach((group) => {
    const keySpan = group.querySelector('span');  // ex. id="nickname"
    const input = group.querySelector('input');   // 해당 input

    if (keySpan && input) {
      updatedData[keySpan.id] = input.value;
    }
  });

  console.log("수정된 데이터:", updatedData);
  store.updateUserInfo(updatedData);
};

const onSubmit2 = (e) => {
  const input = e.target.querySelector('input');
  const key = e.target.querySelector('p')?.id;
  console.log('수정된 데이터')
  console.log(input.value+" "+key)

  if (input && key) {
    const updatedData = {
      [key]: input.value
    };
    console.log("연봉 수정 데이터:", updatedData);
    store.updateUserInfo(updatedData);
  } else {
    console.warn("입력값 또는 키를 찾을 수 없습니다.");
  }
};

</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

img {
    width: 100%;
    max-width: 200px;    // ✅ 최대 너비 지정
    height: auto;        // ✅ 비율 자동 유지
    border-radius: 50%;  // 프로필 원형 이미지일 경우
    display: block;
  }

.custom-container {
  display: flex;
  // justify-content: center;
  // align-items: flex-start;
  margin-top: 4%;
  gap: 40px;

  @media (max-width: 1140px) {
    flex-direction: column;
    align-items: center;
  }
}

.custom-container2 {
  display: flex;  
  // justify-content: flex-end;
  width: 100%;         // ✅ 반응형으로 기본 100% 차지
  margin-left: 20%;
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

.update-button-container {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px; /* Adjust or remove as needed */
}

.pTag {
  margin-bottom: 40px; 
  margin-left: -50px;
}

</style>
