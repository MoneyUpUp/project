<template>
	<div class="full-width">
		<h3>찜 목록</h3>
		<AccessionList :items="store.favoriteList_deposits"/>
		<div class="button-right">
			<DeleteButton />
		</div>

		<hr>

		<h3>
			이자율 비교
		</h3>
	</div>
</template>

<script setup>
import AccessionList from './accession/AccessionList.vue';
import { useFavoriteStore } from '@/stores/favorite';
import { onMounted } from 'vue';
import { RouterView, useRouter, useRoute } from 'vue-router';
import DeleteButton from '@/components/button/DeleteButton.vue';


const store = useFavoriteStore()
const route = useRoute();

onMounted(()=> {
	store.getFavoriteList()
	console.log(store.favoriteList_deposits)
})

</script>

<style scoped>
.full-width {
	margin-top: 8%;
}

.button-right {
  display: flex;
  justify-content: flex-end;
  margin: 1rem 0;
}
</style>
