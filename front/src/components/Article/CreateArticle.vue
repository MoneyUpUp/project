<template>
	<div>
		<form @submit.prevent="onSubmit">
			<div class="mb-3">
				<label for="exampleFormControlInput1" class="form-label">제목</label>
				<input type="text" class="title form-control" id="exampleFormControlInput1" placeholder="제목을 입력하세유" v-model="title">
			</div>
			<div class="mb-3">
				<label for="exampleFormControlTextarea1" class="form-label">글</label>
				<textarea class="content form-control" id="exampleFormControlTextarea1" rows="3" v-model="content"></textarea>
			</div>
			<div class="mb-3" style="display: flex; justify-content: flex-end;">
				<button class="save">저장</button>
			</div>
		</form>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/Articles'

const title = ref('')
const content = ref('')

const articleStore = useArticleStore()

// 로그인할 때 userId가 넘어오게 하면 author에 데이터를 넣을 수 있을듯
// 로그인할 때 localStorage.setItem('userId', res.data.userId)
// 이렇게 받을 수 있으면 딱 좋을 듯
// author 때문에 자꾸 에러남;;
const onSubmit = async (e) => {
  const userId = localStorage.getItem('userId')  // author ID가 필요하다면

  if (!title.value || !content.value) {
    alert('제목과 내용을 모두 입력해주세요.')
    return
  }

  await articleStore.addArticle({
    title: title.value,
    content: content.value,
    author: 1
  })
}
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

.save {
	height: 40px;
	width: 70px;
	background-color: $primary-500;
	color:#fff;
	border-radius: 28px;
}
</style>