<template>
<div>
	<form role="search" style="display: flex;">
    <div class="update-bar">
      <input type="text" id="updateUser" class="updateInput" value="">
    </div>
    <UpdateButton/>
	</form>
</div>
</template>

<script setup>
import UpdateButton from './UpdateButton.vue';
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

.update-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0px;
  gap: 4px;

  position: relative;
  width: 250px;
  max-width: 720px;
  height: 46px;

  background: #ffffff;
  border-radius: 28px;
  padding: 0 16px; /* 내부 여백 추가 */
  box-sizing: border-box;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.update-bar input[type="search"] {
  flex-grow: 1;
  border: none;
  background: transparent;
  outline: none;
  font-size: 16px;
  color: #333;
}

.update-bar
.update-bar .update-btn {
  background: none;
  border: none;
  cursor: pointer;
}

/* 버튼 내부 이미지 스타일링 */
.update-bar button img {
  width: 60px;     /* 아이콘 크기에 맞게 조절 */
  height: 60px;
  object-fit: contain;
}


</style>