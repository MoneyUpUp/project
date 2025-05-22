<template>
	<div class="container">
		<h3 style="margin-bottom: 30px; margin-top: 60px;">Service</h3>
		<div class="row row-cols-1 row-cols-md-3 g-5" >
			<div class="col" v-for="(service, idx) in serviceList" :key="idx">
				<homeServiceItem :service="service" />
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue';
import homeServiceItem from './homeServiceItem.vue';

const serviceList=[
	{title:'금융 챗봇', content:'상냥한 남친 컨셉', path:'', bg:'#43B883'},
	{title:'금융 챗봇', content:'상냥한 여친 컨셉', path:'', bg:'#D9F1E6'},
	{title:'금융 챗봇', content:'박력 테토남 컨셉', path:'', bg:'#43B883'},
]
</script>

<style scoped>
h3 {
	font-family: 'Pretendard', sans-serif;
	color: #43B883;
	font-weight: 600;
}
</style>