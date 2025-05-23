<template>
	<div class="back">

		<div class="container">
			<h3>금 / 은 가격 변동</h3>
			<hr>
			<div style="display: flex;">
				<div style="margin-right: 5%;">
					<label for="startday">시작일 :</label>
					<Datepicker v-model="startday" />
				</div>
				<div> 
					<label for="endday">종료일 :</label>
					<Datepicker v-model="endday" />
				</div>
			</div>
			<silverGraph/>
		</div>
	</div>
</template>

<script setup>
import silverGraph from '@/components/silver/silverGraph.vue'
import Datepicker from 'vue3-datepicker'
import {ref} from 'vue'	

const today = new Date()
const startday = ref(today)
const endday = ref(today)

</script>

<style scoped>

h3 {
	margin-top: 5%;
	font-family: pretendard, sans-serif;
	color: #43B883;
}
</style>