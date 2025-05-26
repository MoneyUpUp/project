<template>
    <div>
        <hr style="margin: 5px auto">
        <table class="table">
            <thead>
                <tr>
                    <th scope="col" class="tableSt" style="width:5%">
                        <input type="checkbox" name="" id="">
                    </th>
                    <th style="width:10%">
                        이미지
                    </th>
                    <th scope="col" style="width:30%">예 적금 명</th>
                    <th scope="col" class="tableSt" style="width:5%">종류</th>
                    <th scope="col" class="tableSt" style="width:20%">가입대상</th>
                    <th scope="col" class="tableSt" style="width:20%">가입방법</th>
                </tr>
            </thead>
            <tbody>
                <AccessionListItem
                v-for="item in items"
                :key="`${item.bank.fin_co_no}-${item.fin_prdt_cd}`"
                :item="item"
                />
            </tbody>
        </table>
    </div>
</template>

<script setup>
import AccessionListItem from './AccessionListItem.vue';
defineProps({
  items: Array
})
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

.tableSt {
    text-align: center;
}
</style>
