<template>
  <BaseModal
    v-if="product"
    @close="$emit('close')"
  >
    <div class="modal-header">
      <h2>{{ product.fin_prdt_nm }}</h2>
      <p class="bank-name">{{ product.bank.kor_co_nm }}</p>
    </div>

    <div class="modal-body">
      <section>
        <h3>가입 정보</h3>
        <p><strong>가입 대상: </strong>{{ product.join_member }}</p>
        <p>
          <strong>가입 방법: </strong>
          <span v-if="Array.isArray(product.join_way)">
            {{ product.join_way.join(', ') }}
          </span>
          <span v-else>{{ product.join_way }}</span>
        </p>
      </section>

      <section v-if="product.options && product.options.length">
        <h3>금리 정보</h3>
        <table>
          <thead>
            <tr>
              <th>기간 (개월)</th>
              <th>이율</th>
              <th>최고 이율</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="option in product.options"
              :key="option.save_trm"
            >
              <td>{{ option.save_trm }}</td>
              <td>{{ option.intr_rate }}%</td>
              <td>{{ option.intr_rate2 }}%</td>
            </tr>
          </tbody>
        </table>
      </section>

      <section>
        <h3>기타 정보</h3>
        <p><strong>우대 조건:</strong> {{ product.spcl_cnd }}</p>
        <p><strong>만기 이자 설명:</strong></p>
        <pre>{{ product.mtrt_int }}</pre>
        <p><strong>기타 설명:</strong></p>
        <pre>{{ product.etc_note }}</pre>
      </section>
    </div>
    <div class="modal-footer">
      <BaseButton
        type="secondary"
        @click="$emit('close')"
        >닫기</BaseButton
      >
      <BaseButton type="primary" @click="handleFavoriteClick">장바구니 추가</BaseButton>
    </div>
  </BaseModal>
</template>

<script setup>
import BaseModal from '@/components/base/BaseModal.vue'
import BaseButton from '../base/BaseButton.vue'
import { useFavoriteStore } from '@/stores/favorite'
const favoriteStore = useFavoriteStore()

const props = defineProps({
  product: Object,
})

const emit = defineEmits(['close'])

const bankColorMap = {
  우리은행: 'bg-woori',
  국민은행: 'bg-kb',
  신한은행: 'bg-shinhan',
  하나은행: 'bg-hana',
  농협은행: 'bg-nh',
  // 추가 은행은 여기에...
}

const handleFavoriteClick = () => {
  favoriteStore.addFavorite(props.product)
}

// const bankColorClass = computed(() => bankColorMap[props.product?.bank.kor_co_nm] || 'bg-default')
</script>

<style scoped>
.modal-header {
  padding: 1rem;
  border-bottom: 1px solid #ccc;
  text-align: center;
}

h2 {
  font-size: 1.75rem;
  margin-bottom: 0.25rem;
}

.bank-name {
  font-weight: bold;
  color: #fff;
  background: rgba(0, 0, 0, 0.25);
  display: inline-block;
  margin-left: 12px;
  padding: 0.2rem 0.5rem;
  border-radius: 0.3rem;
}

.modal-body {
  padding: 1rem;
}

section {
  margin-bottom: 1.5rem;
}

section h3 {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.3rem;
}

p {
  margin: 0.25rem 0;
}

pre {
  white-space: pre-wrap;
  font-size: 0.95rem;
  background: #f9f9f9;
  padding: 0.5rem;
  border-radius: 0.3rem;
}

/* 은행별 배경색 클래스 */
.bg-woori {
  background-color: #4868a5;
  color: white;
}
.bg-kb {
  background-color: #f4b601;
  color: black;
}
.bg-shinhan {
  background-color: #003478;
  color: white;
}
.bg-hana {
  background-color: #009490;
  color: white;
}
.bg-nh {
  background-color: #2a6ae0;
  color: white;
}
.bg-default {
  background-color: #eee;
  color: black;
}

/* 테이블 스타일 */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
th,
td {
  border: 1px solid #ccc;
  padding: 0.4rem;
  text-align: center;
}
th {
  background-color: #f0f0f0;
}

.modal-footer {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  padding: 1rem;
  border-top: 1px solid #eee;
}
</style>
