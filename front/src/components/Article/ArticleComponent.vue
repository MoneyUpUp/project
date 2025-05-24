<template>
	<div class="container">
		<div style="display: flex; justify-content: space-between; align-items: center;">
			<h4>전체 46</h4>

			<div style="display: flex; gap: 12px; align-items: center;">

				<form class="search-bar" role="search">
					<button type="button" class="menu-btn">
						<img src="@/assets/icon/something.png" alt="메뉴" />
					</button>
					<input type="search" placeholder="검색어를 입력하세요" id="searchArticle" class="searchInput">
					<button type="submit" class="search-btn">
						<img src="@/assets/icon/searchicon.png" alt="검색" />
					</button>
				</form>
				<form class="create-bar" role="create" @submit.prevent="onCreate">
					<button type="submit" class="create-btn">게시글 등록</button>
				</form>
			</div>
		</div>
		<p>
			<strong>!</strong> 비방이나 욕설이 담긴 게시물, 개인정보가 포함된 게시물, 신고된 게시물의 경우 별도의 안내 없이 미노출 처리 될 수 있습니다.
		</p>
		<ArticleList/>
	</div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import ArticleList from './ArticleList.vue';

const router = useRouter()
const onCreate = () => {
  router.push('/article/create');
};

</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

p{
	margin-top: 2%;
	font-family: $font-base;
	color: $gray-500;
}
h3 {
	margin-top: 5%;
	font-family: $font-base;
	color: $primary-500;
}

h4 {
	font-family: $font-base;
	color: $primary-500;
}

.create-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0px;
  gap: 4px;

  position: relative;
  width: 120px;
  height: 46px;

  background:$primary-500;
  border-radius: 28px;

  box-sizing: border-box;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.148);
}

.create-btn {
	color:#ffffff;
	font-family: $font-base;
	text-align: center;
	cursor: pointer;

	width: 100%;
  height: 100%;

	display: flex;
  align-items: center;
  justify-content: center;

	border: none; /* 기본 버튼 테두리 제거 */
  background: transparent; /* 배경은 부모(form)가 가짐 */

	font-size: $font-size-base;
  border-radius: 28px;
}

.search-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0px;
  gap: 4px;

  position: relative;
  width: 300px;
  max-width: 720px;
  height: 46px;

  background: #ffffff;
  border-radius: 28px;
  padding: 0 16px; /* 내부 여백 추가 */
  box-sizing: border-box;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.search-bar input[type="search"] {
  flex-grow: 1;
  border: none;
  background: transparent;
  outline: none;
  font-size: 16px;
  color: #333;
}

.search-bar .menu-btn,
.search-bar .search-btn {
  background: none;
  border: none;
  cursor: pointer;
}

/* 버튼 내부 이미지 스타일링 */
.search-bar button img {
  width: 14px;     /* 아이콘 크기에 맞게 조절 */
  height: 14px;
  object-fit: contain;
}
</style>