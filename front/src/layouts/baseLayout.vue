<template>
  <div class="layout-wrapper">
    <BaseNavBar />
    <div class="content-area">
      <RouterView />
    </div>

    <!-- 챗봇 토글 버튼 -->
    <button class="chat-toggle-btn" @click="chat.toggleChat">
      💬
    </button>

    <!-- 챗봇 창 -->
    <div v-if="chat.isChatOpen" class="chatbot-popup">
      <ChatBot />
    </div>
  </div>
</template>

<script setup>
import BaseNavBar from '@/components/layouts/nav/BaseNavBar.vue'
import ChatBot from '@/components/chatbot/ChatBot.vue'
import { RouterView } from 'vue-router'
import { useChatStore } from '@/stores/chatStore'

const chat = useChatStore()
</script>

<style scoped lang="scss">
.layout-wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.content-area {
  flex: 1;
  overflow-y: auto;
  background: var(--bg-color);
}

.chat-toggle-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #000;
  color: white;
  border: none;
  padding: 14px;
  border-radius: 50%;
  font-size: 20px;
  cursor: pointer;
  z-index: 999;
}

.chatbot-popup {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 320px;
  height: 500px;
  background-color: white;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  overflow: hidden; // 내부 컴포넌트에 스크롤 위임
  display: flex;
  flex-direction: column;
  z-index: 998;
}
</style>
