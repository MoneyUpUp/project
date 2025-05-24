<template>
  <div class="container-lg">
    <div class="custom-container">
      <img src="@/assets/profile.png">

      <div style="padding-left: 33px;">
        <p class="name">이지언</p>

        <div class="info-update">
          <span class="info">닉네임</span>
          <UpdateButton/>
        </div>

        <div class="info-update">
          <span class="info">이메일</span>
          <UpdateButton/>
        </div>
        
        <div class="info-update">
          <span class="info">나이</span>
          <UpdateButton/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import UpdateButton from '../button/UpdateButton.vue';
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

img {
  width: 30%;
  height: 30%;
}

.custom-container{
  display: flex;
  padding-top: 70px;
  margin:auto 130px;
}

.name {
  font-family: $font-base;
  font-size: 32px;
  font-weight: 700;
}

.info {
  font-weight: 700;
  padding-top: 10px;
  padding-bottom: 60px;
}

.info-update {
  display: flex;
}


</style>