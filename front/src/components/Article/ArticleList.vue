<template>
	<div>
		<hr style="margin-bottom: 5px;">
		<table class="table">
			<thead>
				<tr>
					<th scope="col" style="width:5%">#</th>
					<th scope="col" style="width:15%">카테고리</th>
					<th scope="col" style="width:50%">제목</th>
					<th scope="col" style="width:15%">작성자</th>
					<th scope="col" style="width:15%">등록일</th>
				</tr>
			</thead>
			<tbody>
				<ArticleListItem v-for="i in 20" :key="i"/>
			</tbody>
		</table>
	</div>
</template>

<script setup>
import ArticleListItem from './ArticleListItem.vue';
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

th {
	text-align: center;
	font-family: $font-base;
	font-size: $font-size-lg;
	color: $primary-500;
}

</style>