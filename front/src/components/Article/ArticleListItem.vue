<template>
	<tr @click="onclick">
		<th style="text-align: center;" scope="row">{{ article.id }}</th>
		<td style="text-align: center;">자유게시판</td>
		<td >{{ article.title }}</td>
		<td style="text-align: center;">{{ article.author }}</td>
		<td style="text-align: center;">{{ article.created_at }}</td>
	</tr>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const onclick = () => {
  router.push('/article/detail');
};

defineProps({
  article: Object
})
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