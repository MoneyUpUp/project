<template>
	<div>
		<h1>예적금 리스트 페이지</h1>
		<div class="test">
			<productSelect/>
			<RouterLink to="/product/deposit">예금</RouterLink>
			<RouterLink to="/product/saving">적금</RouterLink>
		</div>
		<RouterView/>
	</div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import productSelect from '@/components/products/productSelect.vue'

</script>

<style scoped>
.test {
	display: flex;
}
</style>