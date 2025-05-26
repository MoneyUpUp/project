<template>
  <div class="selector">
    <p class="title">💬 누구와 대화하시겠습니까?</p>
    <ul>
      <li v-for="(style, key) in styles" :key="key" @click="ai.selectStyle(key)" class="style-option">
        {{ style.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useChatStore } from '@/stores/chatStore'

const ai = useChatStore()

const styles = {
  default: { name: '기본 챗봇' },
  loopy: { name: '잔망루피' },
  granny: { name: '욕쟁이 할머니' },
  cat: { name: '나대는 고양이' },
  assistant: { name: '상냥한 비서' },
  idol: { name: '하이텐션 아이돌' },
  edgelord: { name: '중2병 천재' },
  cold: { name: '시크한 상담사' },
}
</script>

<style scoped lang="scss">
.selector {
  padding: 24px;
  text-align: center;

  .title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 20px;
  }

  ul {
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .style-option {
    background: #f5f5f5;
    border-radius: 12px;
    padding: 12px 16px;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #e0e0e0;
    }
  }
}
</style>
