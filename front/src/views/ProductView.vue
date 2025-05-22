<template>
	<div class="back">
		<div class="container">
			<!-- <h1>예적금 리스트 페이지</h1> -->
			
			<productHeader style="padding-top: 5%;"/>
			<RouterView/>
		</div>
	</div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import productHeader from '@/components/products/productHeader.vue'

</script>

<style scoped>
.back{
	background: linear-gradient(to top, #d6f3e5, #ffffff);
}
</style>