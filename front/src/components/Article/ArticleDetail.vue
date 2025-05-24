<template>
	<div>
		<form>
			<div class="mb-3">
				<label for="exampleFormControlInput1" class="form-label">제목</label>
				<input type="text" class="title form-control" id="exampleFormControlInput1" placeholder="제목을 입력하세유">
			</div>
			<div class="mb-3">
				<label for="exampleFormControlTextarea1" class="form-label">글</label>
				<textarea class="content form-control" id="exampleFormControlTextarea1" rows="3">마라탕 먹고 싶따</textarea>
			</div>
			<div class="mb-3" style="display: flex; justify-content: flex-end;">
				<button class="update">수정</button>
			</div>
		</form>
	</div>
</template>

<script setup>

</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

div {
	font-family: $font-base;
}

.title {
	box-sizing: border-box;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.066);
}

.content {
	border: solid 1px $gray-300;
	border-radius: 5px;
	box-sizing: border-box;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.066);
	height: 500px;
}

.update {
	height: 40px;
	width: 70px;
	background-color: $primary-500;
	color:#fff;
	border-radius: 28px;
}
</style>