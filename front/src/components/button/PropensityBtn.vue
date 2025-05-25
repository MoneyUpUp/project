<template>
<!-- 투자 성향 바 구성 -->
	<div class="investment-style-container">
		<!-- 상단 라벨 + 말풍선 -->
		<div class="style-label">
			<div class="label-bg">나의 투자성향</div>
			<div class="label-arrow"></div>
		</div>

		<!-- 투자성향 바 -->
		<div class="style-bar">
			<div class="style-box">안정형</div>
			<div class="style-box">안정<br>추구형</div>
			<div class="style-box">위험<br>중립형</div>
			<div class="style-box active">적극<br>투자형</div>
			<div class="style-box">공격<br>투자형</div>
		</div>
	</div>
</template>

<script setup>

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
  left: calc(51.12px * 3); /* 4번째 박스 위에 */
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