<template>
	<div>
		<h1>예적금 리스트 페이지</h1>
		<div class="test">
			<productHeader/>
		</div>
		<RouterView/>
	</div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import productHeader from '@/components/products/productHeader.vue'

</script>

<style scoped>
.test {
	display: flex;
}
</style>