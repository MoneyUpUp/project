<template>
	<div>
		  <div class="signup-container">
				<singUpComponent />
			</div>
	</div>
</template>

<script setup>
import singUpComponent from '@/components/signup/singUpComponent.vue';
</script>

<style scoped>
.signup-container {
  width: 100vw;
  height: 100vh;
  background: linear-gradient(to bottom, #d6f3e5, #ffffff);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>