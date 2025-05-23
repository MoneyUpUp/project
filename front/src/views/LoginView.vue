<template>
	<div>
		  <div class="signup-container">
				<logInComponent />
			</div>
	</div>
</template>

<script setup>
import logInComponent from '@/components/login/logInComponent.vue'
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