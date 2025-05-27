<template>
  <div class="container spot-container">


    <div class="commodity-list-wrapper">
      <h2>주요 원자재 가격</h2>
      <div class="commodity-table">
        <div class="table-header">
          <div class="header-item">원자재</div>
          <div class="header-item">현재 가격</div>
          <div class="header-item">전일 대비</div>
        </div>
        <div class="table-body">
          <div class="table-row" v-for="item in mainCommodities" :key="item.name" @click="selectCommodityFromTable(item.value)">
            <div class="row-item">{{ item.name }}</div>
            <div class="row-item">{{ item.price }}</div>
            <div
              class="row-item"
              :class="{
                'positive': typeof item.change === 'number' && item.change > 0,
                'negative': typeof item.change === 'number' && item.change < 0
              }"
            >
              <template v-if="typeof item.change === 'number'">
                {{ item.change > 0 ? '+' : '' }}{{ item.change }}%
              </template>
              <template v-else>
                {{ item.change }}
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
        <div class="spot-header">
      <BaseSelect
        v-model="store.selectedCommodity"
        placeholder="원자재 명"
        :options="store.commodityOptions"
        style="min-width: 220px"
      />

      <div class="date-range">
        <div class="datepicker-button">
          <label for="startday">시작일</label>
          <Datepicker v-model="store.startDate" />
        </div>
        <div class="datepicker-button">
          <label for="endday">종료일</label>
          <Datepicker v-model="store.endDate" />
        </div>
      </div>
    </div>

    <div class="chart-wrapper">
      <silverGraph v-show="store.selectedData.length > 0" />
      <p v-if="store.selectedData.length === 0" class="no-data-message">선택된 기간에 대한 데이터가 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import BaseSelect from '@/components/base/BaseSelect.vue'
import silverGraph from '@/components/silver/silverGraph.vue' // silverGraph 주석 해제
import Datepicker from 'vue3-datepicker'
import { useSpotAssetStore } from '@/stores/spotAssetStore'
import { computed, onMounted } from 'vue' // watch 제거

const store = useSpotAssetStore()

// 주요 원자재 데이터를 계산하는 computed 속성
const mainCommodities = computed(() => {
  return store.commodityOptions.map(option => {
    const data = store.spotAssetPrices[option.value];

    let price = 'N/A';
    let change = 'N/A';

    if (data && data.length > 0) {
      const latestPrice = data[data.length - 1]?.close_price; // price 대신 close_price 사용
      if (typeof latestPrice === 'number') {
        price = `${latestPrice.toFixed(2)} USD`;
      }

      if (data.length > 1) {
        const previousPrice = data[data.length - 2]?.close_price; // price 대신 close_price 사용
        if (typeof latestPrice === 'number' && typeof previousPrice === 'number' && previousPrice !== 0) {
          const calculatedChange = ((latestPrice - previousPrice) / previousPrice) * 100;
          change = calculatedChange.toFixed(2);
        }
      }
    } else {
      // console.log(`Returning N/A for commodity: ${option.value} due to no data.`); // 디버깅 로그 제거
    }

    return {
      name: option.label.split(' ')[0], // "금 가격 (USD)"에서 "금"만 추출
      value: option.value, // option.value 추가
      price: price,
      change: change,
    };
  });
});

const selectCommodityFromTable = (commodityValue) => {
  store.selectedCommodity = commodityValue;
  // 선택된 원자재의 데이터를 다시 가져올 필요는 없습니다.
  // store의 watchEffect가 selectedCommodity 변경을 감지하여 자동으로 fetchSpotAssetPrices를 호출합니다.
};

onMounted(() => {
  // 모든 주요 원자재 데이터를 미리 가져옵니다.
  store.commodityOptions.forEach(option => {
    store.fetchSpotAssetPrices(option.value);
  });
});
</script>

<style scoped lang="scss">
.spot-container {
  // margin-top: 3rem;
  padding: 2rem; /* 패딩 증가 */
  width: 100%;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  // background-color: #f9f9f9; /* ProductView의 사이드바와 유사한 배경색 */
  border-radius: 12px;
  // box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08); /* 그림자 강조 */
  // border: 1px solid #e0e0e0; /* 테두리 추가 */

  display: flex;
  flex-direction: column;
  gap: 3rem; /* 요소 간 간격 증가 */
}

.spot-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 2rem; /* 헤더 내부 간격 증가 */
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e0e0e0; /* 구분선 색상 조정 */
}

.date-range {
  display: flex;
  gap: 1.2rem; /* 날짜 범위 간격 조정 */
}

.datepicker-button {
  display: flex;
  flex-direction: column;
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
  gap: 0.4rem;

  input {
    padding: 0.6rem 1rem;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background-color: #ffffff; /* 배경색을 흰색으로 변경 */
    color: #374151;
    font-weight: 500;
    cursor: pointer;
    font-size: 15px;
    transition:
      background-color 0.2s ease,
      border-color 0.2s ease,
      box-shadow 0.2s ease;

    &:hover {
      background-color: #f0f0f0; /* 호버 배경색 조정 */
      border-color: #9ca3af;
    }

    &:focus {
      border-color: #4f46e5;
      outline: none;
      background-color: #fff;
      box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
    }
  }
}

.chart-wrapper {
  padding-top: 2.5rem; /* 상단 패딩 증가 */
}

.commodity-list-wrapper {
  h2 {
    font-size: 1.8rem;
    color: #2c3e50;
    margin-bottom: 1.5rem;
    text-align: center;
    font-weight: 700;
  }
}

.commodity-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #ffffff;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);

  .table-header, .table-row {
    display: flex;
    padding: 1rem 1.5rem;
    border-bottom: 1px solid #f0f0f0;
    align-items: center;
  }

  .table-header {
    background-color: #eef2f7;
    font-weight: 700;
    color: #555;
    font-size: 1rem;
    text-transform: uppercase;
  }

  .table-row {
    font-size: 0.95rem;
    color: #333;
    transition: background-color 0.2s ease;

    &:hover {
      background-color: #f8fafd;
    }

    &:last-child {
      border-bottom: none;
    }
  }

  .header-item, .row-item {
    flex: 1;
    text-align: center;

    &:nth-child(1) { text-align: left; flex: 1.5; }
    &:nth-child(2) { text-align: right; }
    &:nth-child(3) { text-align: right; flex: 0.8; }
  }

  .positive {
    color: #28a745; /* Green for positive change */
    font-weight: 600;
  }

  .negative {
    color: #dc3545; /* Red for negative change */
    font-weight: 600;
  }
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .spot-container {
    padding: 1rem; /* 모바일 패딩 조정 */
    margin-top: 2rem;
  }
  .spot-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem; /* 모바일 헤더 내부 간격 조정 */
  }

  .date-range {
    width: 100%;
    flex-direction: column;
    gap: 0.8rem;
  }

  .datepicker-button {
    width: 100%;
  }

  .commodity-table {
    .table-header, .table-row {
      padding: 0.8rem 1rem;
      font-size: 0.85rem;
    }
    .header-item, .row-item {
      &:nth-child(1) { flex: 1.2; }
      &:nth-child(2) { flex: 1; }
      &:nth-child(3) { flex: 0.8; }
    }
  }
}
</style>
