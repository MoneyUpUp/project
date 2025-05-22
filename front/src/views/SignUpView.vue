<template>
	<div>
		<h1>회원가입 페이지</h1>
		<form @submit.prevent="onSignup">
			<label for="username">username : </label>
			<input type="text" id="username" v-model="username">
			<br>
			<label for="password1">password1 : </label>
			<input type="password1" id="password1" v-model="password1">
			<br>
			<label for="password2">password2 : </label>
			<input type="password2" id="password2" v-model="password2">
			<input type="submit" value="signup">
			<br>
		</form>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const username = ref('')
const password1 = ref('')
const password2 = ref('')

const store = useAccountStore()
const onSignup = function() {
    const userInfo = {
        username : username.value,
        password1 : password1.value,
        password2 : password2.value,
    }

    store.createUser(userInfo)
}
</script>

<style scoped>

</style>