<template>
<div>
	<form class="search-bar" role="search">
		<button type="button" class="menu-btn">
		</button>
		<input type="search" id="searchArticle" class="searchInput" value="">
		<button type="submit" class="search-btn">
			<img src="@/assets/icon/update.png" alt="검색" />
		</button>
	</form>
</div>
</template>

<script setup>

</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

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

.search-bar
.search-bar .search-btn {
  background: none;
  border: none;
  cursor: pointer;
}

/* 버튼 내부 이미지 스타일링 */
.search-bar button img {
  width: 60px;     /* 아이콘 크기에 맞게 조절 */
  height: 60px;
  object-fit: contain;
}


</style>