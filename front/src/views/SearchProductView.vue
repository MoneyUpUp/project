<template>
	<div class="container">
		<h3>관심 종목 검색</h3>
		<hr>
        <form @submit.prevent="onclick">
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="원하는 종목을 검색해보세요" id="company" ref="companyInput">
            <button class="btn btn-outline-secondary" type="submit">
                <img src="@/assets/icon/searchicon.png" alt="검색" />
            </button>
        </div>
        </form>
        <RouterView/>
    </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import { ref } from 'vue'
import { useSearchStore } from '@/stores/searchVideo'

const store = useSearchStore()
const companyInput = ref(null)

const onclick = (e) => {
  store.searchCompany(companyInput.value.value)
}


</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

h3 {
	margin-top: 5%;
	font-family: $font-base;
	color: $primary-500;
}
</style>