<template>
	<button class="update-btn">수정</button>
</template>

<script setup>

</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

.update-btn {
  display: flex;
  flex-direction: row;
  align-items: center;
	justify-content: center;
  gap: 4px;

  position: relative;
  width: 80px;
  height: 46px;
	margin: 0 10px;

  background-color: $primary-500;
	color: #fff;
  border-radius: 28px;
  box-sizing: border-box;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);

}
</style>