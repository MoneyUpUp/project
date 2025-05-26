<template>
  <div class="chatbot-wrapper">
    <ChatStyleSelector v-if="!ai.selectedStyle" />
    <ChatConversation v-else />
  </div>
</template>

<script setup>
import ChatStyleSelector from './ChatStyleSelector.vue'
import ChatConversation from './ChatConversation.vue'
import { useChatStore } from '@/stores/chatStore'

const ai = useChatStore()
</script>

<style scoped lang="scss">
.chatbot-wrapper {
  display: flex;
  flex-direction: column;
  height: 100%; // <- 꼭 필요!
  overflow-y: auto; // 스크롤 가능하게
}
</style>
