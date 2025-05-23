<template>
	<div>
		<h1>프로필페이지</h1>
		<div class="profile-container">

			<profileUpdate/>
		</div>
	</div>
</template>

<script setup>
import profileUpdate from '@/components/profile/profileUpdate.vue';
</script>

<style scoped>
.profile-container {
  width: 100vw;
  height: 100vh;
  background: linear-gradient(to bottom, #d6f3e5, #ffffff);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>