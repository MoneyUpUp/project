<template>
	<div>
		  <div class="signup-container">
        <RouterView/>
			</div>
	</div>
</template>

<script setup>
import { RouterView  } from 'vue-router';
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