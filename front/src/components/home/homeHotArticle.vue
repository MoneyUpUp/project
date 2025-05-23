<template>
  <div>
    <div class="container" style="margin-top: 5%;">
      <h3 style="margin-bottom: 30px; margin-top: 8%;">Article</h3>
      <div class="content">
        <article>
          <h5><strong>"나에게 맞는 금융상품, 어떻게 골라야 할까?"</strong></h5>
          <p>
            우리는 모두 돈을 벌고, 쓰고, 모으며 살아갑니다. 그런데 '어떻게' 쓰고,
            '어디에' 모으느냐에 따라 삶의 방향이 달라질 수 있습니다. 적금, 예금, 펀드, 보험, 주식…
            금융상품은 너무나 많고, 그만큼 선택도 어렵습니다.
            <br /><br />
            내 목표가 단기 자금 마련인지, 장기 자산 증식인지에 따라 전략은 달라져야 해요.
            예를 들어, 몇 개월 후 여행을 위해 돈을 모은다면 정기적금이나 CMA가 적합할 수 있고,
            5년 뒤 내 집 마련을 꿈꾼다면 청년 우대형 주택청약종합저축 같은 정부 지원 상품을 활용할 수도 있죠.
            <br /><br />
            금융은 어렵고 복잡하게 느껴질 수 있지만, 작은 관심과 기초 지식만 있어도
            내게 유리한 조건의 상품을 고를 수 있어요.
            이번 주엔 내가 가입한 금융상품을 한 번 점검해보는 건 어떨까요?
          </p>
        </article>
        <img src="@/assets/birdHi.png" alt="birdHi" />
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
h3 {
  font-family: 'Pretendard', sans-serif;
  color: #43B883;
  font-weight: 600;
}

.content {
  display: flex;
  align-items: center; /* 세로 중앙 정렬 */
  justify-content: space-between; /* 좌우 간격 정렬 */
  gap: 40px; /* 텍스트와 이미지 사이 간격 */
  flex-wrap: wrap; /* 반응형 대응 */
}

article {
  font-family: 'Pretendard', sans-serif;
  width: 485px;
}

img {
  width: 50%;
  height: auto;
  object-fit: contain;
  max-width: 300px; /* 너무 커지지 않게 제한 가능 */
}
</style>
