<template>
    <tr @click="onclick">
		<td style="text-align: center;" scope="row">
            <input 
                type="checkbox" 
                :checked="isSelected" 
                @change="handleCheckboxChange"
                @click.stop
            >
        </td>
        <td>
            <img :src="getBankLogoById(item.bank.fin_co_no)"  style="width: 40%;" alt="">
        </td>

		<td>{{ item.fin_prdt_nm }}</td>
		<td>{{ item.type === 'deposit' ? '예금' : item.type === 'saving' ? '적금' : '기타' }}</td>
		<td style="text-align: center;">{{ item.join_member }}</td>
		<td style="text-align: center;">{{ item.join_way }}</td>
	</tr>
</template>

<script setup>
import { onMounted } from 'vue';
import { getBankLogoById } from '@/constants/banks'
const props = defineProps({
  item: Object,
  isSelected: Boolean
})

const emit = defineEmits(['update:selected'])

const handleCheckboxChange = (event) => {
  console.log(`AccessionListItem - Checkbox for ${props.item.fin_prdt_nm} changed to: ${event.target.checked}`);
  emit('update:selected', event.target.checked);
};

const onclick = () => {
  console.log('AccessionListItem - Row clicked:', props.item);
}

onMounted(()=> {
  console.log('AccessionListItem - Mounted with item:', props.item);
})
</script>

<style scoped>

</style>
