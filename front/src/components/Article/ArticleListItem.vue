<template>
	<tr @click="onclick">
		<th style="text-align: center;" scope="row">1</th>
		<td style="text-align: center;">자유게시판</td>
		<td >저녁 뭐 먹지</td>
		<td style="text-align: center;">이지언</td>
		<td style="text-align: center;">2025-04-20</td>
	</tr>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const onclick = () => {
  router.push('/article/detail');
};
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

tr {
  cursor: pointer;
	font-family: $font-base;
	font-size: $font-size-base;
	color: $primary-500;
}

td {
	padding: 15px;
}
</style>