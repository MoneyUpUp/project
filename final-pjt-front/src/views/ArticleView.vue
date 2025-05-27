<template>
	<div class="container">
		<h3>커뮤니티</h3>
		<hr>
		<RouterView/>
	</div>
</template>

<script setup>
import { RouterView } from 'vue-router';
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

h3 {
	margin-top: 5%;
	font-family: $font-base;
	color: $primary-500;
}
</style>