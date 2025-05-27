<template>
<!-- 투자 성향 바 구성 -->
	<div class="investment-style-container">

		<!-- 투자성향 바 -->
		<div class="style-bar">
			<div 
        v-for="(style, index) in styles" 
        :key="style.id"
        class="style-box"
        :class="{ active: activeIndex === index }"
        @click="selectStyle(index)"
        v-html="style.text"
      >
      </div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAccountStore } from '@/stores/accounts';

const store = useAccountStore();

const styles = ref([
  { text: '3개월', id: 0 },
  { text: '6개월', id: 1 },
  { text: '1년', id: 2 },
  { text: '1년6개월', id: 3 },
  { text: '5년 이상', id: 4 }
]);

const activeIndex = ref(3); // 초기 활성 인덱스, 필요에 따라 0 또는 다른 값으로 변경 가능

const selectStyle = (index) => {
  activeIndex.value = index;
  const selectedText = styles.value[index].text.replace('<br>', '');
  store.setPeriod(selectedText); // setPeriod 액션 사용
  localStorage.setItem('userPeriod', selectedText);
  // console.log("Selected period index:", index, "Text:", selectedText);
};

onMounted(() => {
  const savedPeriod = localStorage.getItem('userPeriod');
  if (savedPeriod) {
    const foundIndex = styles.value.findIndex(style => style.text.replace('<br>', '') === savedPeriod);
    if (foundIndex !== -1) {
      activeIndex.value = foundIndex;
      store.setPeriod(savedPeriod); // setPeriod 액션 사용
      // console.log('저장된 기간 불러옴:', savedPeriod, '인덱스:', foundIndex);
    }
  }
});


</script>

<style scoped>
.investment-style-container {
  position: relative;
  width: fit-content;
  margin:  auto;
	transform: scale(1.2); 
  transform-origin: top left;
	
	@media (min-width: 768px) {
    transform: scale(1.1);
  }
}

.style-label {
  position: absolute;
  /* left is now set dynamically via :style binding */
  top: -24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2;
}

.label-bg {
  background: #8ED4B5;
  color: #fff;
  font-size: 8px;
  font-weight: 500;
  border-radius: 2px;
  padding: 2px 6px;
  line-height: 1.4;
  white-space: nowrap; /* Prevent text wrapping in label */
}

.label-arrow {
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid #8ED4B5;
  margin-top: -1px;
}

.style-bar {
  display: flex;
  position: relative;
  z-index: 1;
}

.style-box {
  width: 51.12px;
  height: 37.96px;
  background: #fff;
  border: 1px solid #d9d9d9;
  font-size: 13px;
  font-weight: 300;
  color: #000;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  line-height: 1.2;
  letter-spacing: -0.04em;
  box-sizing: border-box;
  cursor: pointer; /* Add pointer cursor on hover */
}

.style-box:first-child {
  border-radius: 5px 0 0 5px;
}

.style-box:last-child {
  border-radius: 0 5px 5px 0;
}

.style-box.active {
  background: #D9F1E6;
  border: 1px solid #43B883;
  color: #43B883;
}
</style>
