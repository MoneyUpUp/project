<template>
  <div>
    <h2>맞춤상품추천</h2>

    <h3>예금 추천</h3>
    <div
      v-if="depositRecommendations.length"
      class="recommendations-grid"
    >
      <BaseCard
        v-for="rec in depositRecommendations"
        :key="rec.id"
        class="recommendation-card"
      >
        <img
          :src="getBankLogoById(rec.bank_id)"
          alt="은행 로고"
          class="bank-logo"
        />
        <p class="product-name"><strong>상품명:</strong> {{ rec.name }}</p>
        <p><strong>은행:</strong> {{ rec.bank }}</p>
        <p><strong>기간:</strong> {{ rec.save_trm }}개월</p>
        <p class="interest-rate"><strong>금리:</strong> {{ rec.interest_rate }}%</p>
        <p class="recommendation-reason"><strong>추천 이유:</strong> {{ rec.reason }}</p>
      </BaseCard>
    </div>
    <div
      v-else
      class="no-recommendations"
    >
      <p>추천할 예금 상품이 없습니다.</p>
    </div>

    <h3>적금 추천</h3>
    <div
      v-if="savingRecommendations.length"
      class="recommendations-grid"
    >
      <BaseCard
        v-for="rec in savingRecommendations"
        :key="rec.id"
        class="recommendation-card"
      >
        <img
          :src="getBankLogoById(rec.bank_id)"
          alt="은행 로고"
          class="bank-logo"
        />
        <p class="product-name"><strong>상품명:</strong> {{ rec.name }}</p>
        <p><strong>은행:</strong> {{ rec.bank }}</p>
        <p><strong>기간:</strong> {{ rec.save_trm }}개월</p>
        <p class="interest-rate"><strong>금리:</strong> {{ rec.interest_rate }}%</p>
        <p class="recommendation-reason"><strong>추천 이유:</strong> {{ rec.reason }}</p>
      </BaseCard>
    </div>
    <div
      v-else
      class="no-recommendations"
    >
      <p>추천할 적금 상품이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import BaseCard from '@/components/base/BaseCard.vue' // BaseCard 컴포넌트 임포트
import { getBankLogoById } from '@/constants/banks.js' // 은행 로고 함수 임포트
import axios from 'axios'
import { computed, onMounted, ref } from 'vue'

const recommendations = ref([])

const depositRecommendations = computed(() => {
  return recommendations.value.filter((rec) => rec.type === 'deposit')
})

const savingRecommendations = computed(() => {
  return recommendations.value.filter((rec) => rec.type === 'saving')
})

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/ai/recommend/', {
      headers: {
        Authorization: `Token ${localStorage.getItem('token')}`,
      },
    })
    recommendations.value = response.data.recommendations
    console.log(recommendations.value)
  } catch (error) {
    console.error('추천 상품을 불러오는 데 실패했습니다:', error)
  }
})
</script>

<style scoped>
div {
  padding: 20px;
  font-family: 'Noto Sans KR', sans-serif; /* 폰트 적용 */
  color: #333;
}

h2 {
  font-size: 2.2em;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 40px;
  font-weight: 700;
  position: relative;
}

h2::after {
  content: '';
  display: block;
  width: 60px;
  height: 4px;
  background-color: #42b983;
  margin: 10px auto 0;
  border-radius: 2px;
}

h3 {
  font-size: 1.8em;
  color: #34495e;
  margin-top: 30px;
  margin-bottom: 25px;
  border-bottom: 2px solid #eee;
  padding-bottom: 10px;
  font-weight: 600;
}

.recommendations-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
  margin-bottom: 40px;
}

.recommendation-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  background-color: #ffffff;
}

.recommendation-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.bank-logo {
  width: 70px;
  height: 70px;
  margin-bottom: 15px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #eee;
}

.product-name {
  font-size: 1.3em;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 10px;
}

.recommendation-card p {
  margin: 4px 0;
  line-height: 1.6;
  color: #555;
}

.recommendation-card p strong {
  color: #333;
}

.interest-rate {
  font-size: 1.1em;
  font-weight: 700;
  color: #e74c3c; /* 강조 색상 */
  margin-top: 10px;
  margin-bottom: 10px;
}

.recommendation-reason {
  font-style: italic;
  color: #7f8c8d;
  font-size: 0.95em;
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px dashed #eee;
}

.no-recommendations {
  text-align: center;
  padding: 30px;
  background-color: #f0f4f8;
  border-radius: 10px;
  color: #7f8c8d;
  font-size: 1.1em;
  margin-bottom: 40px;
}
</style>
