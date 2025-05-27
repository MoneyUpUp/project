<template>
  <div class="layout-wrapper">
    <BaseNavBar />
    <div class="content-area">
      <RouterView />
    </div>

    <!-- 챗봇 토글 버튼 -->
    <button class="chat-toggle-btn" @click="chat.toggleChat">
      <Transition name="slide-fade"> <!-- mode="out-in" 제거 -->
        <img :src="currentImage" :key="currentImage" alt="Chatbot Toggle" class="chat-toggle-img" />
      </Transition>
    </button>

    <!-- 챗봇 창 -->
    <div v-if="chat.isChatOpen" class="chatbot-popup">
      <ChatBot />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'; // watch 임포트 추가
import BaseNavBar from '@/components/layouts/nav/BaseNavBar.vue'
import ChatBot from '@/components/chatbot/ChatBot.vue'
import { RouterView } from 'vue-router'
import { useChatStore } from '@/stores/chatStore.js'

const chat = useChatStore()

// 챗봇 스타일에서 이미지 경로 목록 생성
const styleImagePaths = Object.values(chat.styles).map(
  (style) => `/src/assets/images/chatbots/${style.default}.png`
);

const currentImage = ref(''); // 현재 표시될 이미지 (초기값 빈 문자열)
let intervalId;

// 챗봇 스타일이 선택되었는지 여부에 따라 이미지 설정
const updateImage = () => {
  if (chat.selectedStyle) {
    // 특정 스타일이 선택된 경우 해당 스타일 이미지로 고정
    const selectedStylePath = `/src/assets/images/chatbots/${chat.selectedStyle}.png`;
    currentImage.value = selectedStylePath;
    if (intervalId) {
      clearInterval(intervalId); // 랜덤 변경 중지
      intervalId = null;
    }
  } else {
    // 스타일이 선택되지 않은 경우 랜덤 이미지 변경 시작
    if (!intervalId) {
      intervalId = setInterval(() => {
        const randomIndex = Math.floor(Math.random() * styleImagePaths.length);
        currentImage.value = styleImagePaths[randomIndex];
      }, 5000); // 5000ms = 5초
    }
    // 초기 로드 시 랜덤 이미지 설정
    if (!currentImage.value) {
      const randomIndex = Math.floor(Math.random() * styleImagePaths.length);
      currentImage.value = styleImagePaths[randomIndex];
    }
  }
};

onMounted(() => {
  updateImage(); // 컴포넌트 마운트 시 초기 이미지 설정
});

onUnmounted(() => {
  // 컴포넌트 언마운트 시 인터벌 정리
  if (intervalId) {
    clearInterval(intervalId);
  }
});

// selectedStyle 변화 감지
watch(() => chat.selectedStyle, (newStyle) => {
  updateImage();
});

// isChatOpen 변화 감지 (챗봇이 닫힐 때 selectedStyle 초기화)
watch(() => chat.isChatOpen, (isOpen) => {
  if (!isOpen && chat.selectedStyle) {
    chat.selectedStyle = null; // 챗봇이 닫히면 선택된 스타일 초기화
    updateImage(); // 이미지 다시 랜덤으로 변경
  }
});
</script>

<style scoped lang="scss">
@use '@/assets/styles/utils/_variables.scss' as *; // _variables.scss 임포트 추가

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
  bottom: 30px;
  right: 30px; /* 오른쪽 하단으로 변경 */
  left: auto; /* 왼쪽 정렬 방지 */
  background-color: transparent; /* 배경색 투명으로 변경 */
  border: none; /* 테두리 제거 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); /* 그림자를 살짝 더 진하게 */
  padding: 0; /* 패딩 제거 */
  border-radius: 50%;
  cursor: pointer;
  z-index: 1000; /* z-index 높임 */
  width: 60px; /* 버튼 크기 고정 */
  height: 60px; /* 버튼 크기 고정 */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* 이미지가 버튼 밖으로 나가지 않도록 */
}

.chat-toggle-img {
  width: 100%; /* 버튼 크기에 맞게 이미지 조절 */
  height: 100%; /* 버튼 크기에 맞게 이미지 조절 */
  object-fit: cover; /* 이미지가 잘리지 않고 채워지도록 */
  border-radius: 50%; /* 이미지도 원형으로 */
  position: absolute; /* 애니메이션을 위해 absolute 포지셔닝 */
  top: 0;
  left: 0;
}

/* 슬라이드 애니메이션 */
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.5s ease-in-out;
}

.slide-fade-enter-from {
  transform: translateX(-100%); /* 왼쪽에서 시작 */
  opacity: 0;
}

.slide-fade-leave-to {
  transform: translateX(-100%); /* 왼쪽으로 사라짐 */
  opacity: 0;
}

.chatbot-popup {
  position: fixed;
  bottom: 100px;
  right: 30px;
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
