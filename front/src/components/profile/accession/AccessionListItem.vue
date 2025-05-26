<template>
    <tr @click="onclick">
		<td style="text-align: center;" scope="row">
            <input type="checkbox" name="" id="">
        </td>
        <td>
            <img :src="getBankLogo(item.bank.kor_co_nm)"  style="width: 40%;" alt="">
        </td>

		<td>{{ item.fin_prdt_nm }}</td>
		<td>{{ item.type === 'deposit' ? '예금' : item.type === 'saving' ? '적금' : '기타' }}</td>
		<td style="text-align: center;">{{ item.join_member }}</td>
		<td style="text-align: center;">{{ item.join_way }}</td>
	</tr>
</template>

<script setup>
defineProps({
  item: Object
})

const getBankLogo = (bankName) => {
  const name = bankName.toLowerCase().replace(/\s/g, '')
  return new URL(`@/assets/images/banks/${name}-bank.png`, import.meta.url).href
}
</script>

<style scoped>

</style>