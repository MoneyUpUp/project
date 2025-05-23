<template>
    <div class="container">
        <h1>Search Video</h1>
        <hr>
        <form @submit.prevent="onclick">
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="search video" id="company" ref="companyInput">
            <button class="btn btn-outline-secondary" type="submit">🔍</button>
        </div>
        </form>

        <searchList/>

    </div>
</template>

<script setup>
import searchList from '@/components/search/searchList.vue'
import { ref } from 'vue'
import { useSearchStore } from '@/stores/searchVideo'

const store = useSearchStore()
const companyInput = ref(null)

const onclick = (e) => {
  store.searchCompany(companyInput.value.value)
  // console.log(companyInput.value.value)
}


</script>
<style scoped>

</style>