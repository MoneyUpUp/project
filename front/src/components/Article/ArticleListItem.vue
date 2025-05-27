<template>
	<tr @click="onclick">
		<th style="text-align: center;" scope="row">{{ article.id }}</th>
		<td style="text-align: center;">자유게시판</td>
		<td >{{ article.title }}</td>
		<td style="text-align: center;">{{ article.author }}</td>
		<td style="text-align: center;">{{ formatDate(article.created_at)  }}</td>
	</tr>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/Articles';
const router = useRouter()
const onclick = () => {
  router.push('/article/detail');
};

defineProps({
  article: Object
})

function formatDate(dateStr) {
	const date = new Date(dateStr);
	const year = date.getFullYear();
	const month = date.getMonth() + 1; // 월은 0부터 시작
	const day = date.getDate();
	return `${year}년 ${month}월 ${day}일`;
}
  
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