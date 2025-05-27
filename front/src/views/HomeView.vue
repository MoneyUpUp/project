<template>
  <div class="home-view" ref="homeViewRef">
    <section id="section-carousel" class="full-screen-section hero-section">
      <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
        <!-- 🔘 인디케이터 버튼 -->
        <div class="carousel-indicators">
          <button v-for="(image, idx) in images" :key="'indicator-' + idx" type="button"
            data-bs-target="#carouselExampleSlidesOnly" :data-bs-slide-to="idx" :class="{ active: idx === 0 }"
            :aria-current="idx === 0 ? 'true' : null" :aria-label="'Slide ' + (idx + 1)">
          </button>
        </div>

        <!-- 🖼️ 슬라이드 이미지 -->
        <div class="carousel-inner">
          <div v-for="(image, idx) in images" :key="'slide-' + idx" :class="['carousel-item', { active: idx === 0 }]">
            <img :src="image" class="d-block w-100 carousel-img" alt="..." />
          </div>
        </div>
      </div>
    </section>

    <section id="section-features" class="full-screen-section features-section">
      <h2>주요 서비스</h2>
      <div class="features-grid">
        <div class="feature-item">
          <img src="@/assets/icon/searchicon.png" alt="금융 상품" class="feature-icon" />
          <h3>금융 상품 추천</h3>
          <p>나에게 딱 맞는 예금, 적금, 대출 상품을 찾아보세요.</p>
        </div>
        <div class="feature-item">
          <img src="@/assets/icon/basicprofile.png" alt="자산 관리" class="feature-icon" />
          <h3>자산 관리</h3>
          <p>나의 자산을 한눈에 확인하고 효율적으로 관리하세요.</p>
        </div>
        <div class="feature-item">
          <img src="@/assets/images/chatbots/default.png" alt="챗봇 상담" class="feature-icon" />
          <h3>AI 챗봇 상담</h3>
          <p>궁금한 금융 정보를 AI 챗봇에게 물어보세요.</p>
        </div>
        <div class="feature-item">
          <img src="@/assets/icon/something.png" alt="커뮤니티" class="feature-icon" />
          <h3>커뮤니티</h3>
          <p>다양한 금융 정보를 공유하고 소통하세요.</p>
        </div>
      </div>
    </section>

    <section id="section-articles" class="full-screen-section latest-articles-section">
      <h2>최신 금융 뉴스 & 게시글</h2>
      <div class="articles-grid">
        <!-- 예시 게시글 아이템 -->
        <div class="article-card">
          <h3>2024년 경제 전망: 투자 전략은?</h3>
          <p>전문가들이 예측하는 2024년 경제 동향과 투자 팁을 확인하세요.</p>
          <a href="#" class="read-more">더 보기</a>
        </div>
        <div class="article-card">
          <h3>청년들을 위한 주택 구매 가이드</h3>
          <p>생애 첫 주택 구매를 위한 대출 상품과 지원 제도를 알아보세요.</p>
          <a href="#" class="read-more">더 보기</a>
        </div>
        <div class="article-card">
          <h3>은퇴 후 안정적인 삶을 위한 연금 계획</h3>
          <p>미래를 위한 현명한 연금 상품 선택과 재정 계획을 세우세요.</p>
          <a href="#" class="read-more">더 보기</a>
        </div>
      </div>
    </section>

    <footer id="section-footer" class="full-screen-section app-footer">
      <div class="footer-content">
        <p>&copy; 2024 MoneyUp. All rights reserved.</p>
        <p>문의: support@moneyup.com | 전화: 02-1234-5678</p>
        <p>서울특별시 강남구 테헤란로 123</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import img1 from '@/assets/banner1.png'
import img2 from '@/assets/banner2.png'

const images = [img1, img2]
const homeViewRef = ref(null)
const sections = ref([])
const currentSectionIndex = ref(0)
let isScrolling = false

const scrollToSection = (index) => {
  if (index >= 0 && index < sections.value.length) {
    isScrolling = true
    sections.value[index].scrollIntoView({ behavior: 'smooth' })
    currentSectionIndex.value = index
    setTimeout(() => {
      isScrolling = false
    }, 1000) // 스크롤 애니메이션 시간에 맞춰 조절
  }
}

const handleWheel = (event) => {
  if (isScrolling) return

  event.preventDefault() // 기본 스크롤 동작 방지

  if (event.deltaY > 0) {
    // 아래로 스크롤
    if (currentSectionIndex.value < sections.value.length - 1) {
      scrollToSection(currentSectionIndex.value + 1)
    }
  } else {
    // 위로 스크롤
    if (currentSectionIndex.value > 0) {
      scrollToSection(currentSectionIndex.value - 1)
    }
  }
}

onMounted(() => {
  sections.value = [
    document.getElementById('section-carousel'),
    document.getElementById('section-features'),
    document.getElementById('section-articles'),
    document.getElementById('section-footer')
  ].filter(Boolean) // null 값 필터링

  if (homeViewRef.value) {
    homeViewRef.value.addEventListener('wheel', handleWheel, { passive: false })
  }
})

onBeforeUnmount(() => {
  if (homeViewRef.value) {
    homeViewRef.value.removeEventListener('wheel', handleWheel)
  }
})
</script>

<style scoped>
html, body {
  overflow: hidden; /* 전체 페이지 스크롤 방지 */
}

.home-view {
  display: flex;
  flex-direction: column;
  background-color: #f8f9fa;
  overflow-y: scroll; /* 섹션 스크롤을 위한 스크롤바 */
  scroll-snap-type: y mandatory; /* 스크롤 스냅 적용 */
  height: calc(100vh - 60px); /* 내비게이션 바 높이 제외 */
  margin-top: 60px; /* 내비게이션 바 아래로 이동 */
  position: relative; /* 추가: 스크롤 컨테이너로서의 역할 명확히 */
}

.full-screen-section {
  height: 100%; /* 부모 요소의 높이를 상속받도록 변경 */
  width: 100vw; /* 뷰포트 너비 꽉 채우기 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  scroll-snap-align: start; /* 스크롤 스냅 시작 지점 */
  flex-shrink: 0; /* 섹션이 줄어들지 않도록 방지 */
  position: relative; /* 자식 요소의 absolute 포지셔닝을 위해 */
  overflow: hidden; /* 내용이 넘칠 경우 숨김 */
}

.hero-section {
  background-color: #f8f9fa; /* 캐러셀 배경색 */
  margin-bottom: 0; /* 기존 마진 제거 */
  padding-top: 0; /* HomeView에 margin-top을 주므로 여기서는 제거 */
}

.carousel-img {
  height: 100%; /* 부모 요소의 높이를 상속받도록 변경 */
  object-fit: cover;
}

.carousel-inner {
  height: 100%; /* 캐러셀 내부 높이 꽉 채우기 */
}

.carousel-item {
  height: 100%; /* 캐러셀 아이템 높이 꽉 채우기 */
}

.carousel-indicators {
  position: absolute;
  bottom: 20px; /* 하단에 위치 */
  z-index: 15;
}

.carousel-indicators [data-bs-target] {
  background-color: #43B883;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin: 0 5px;
  border: 0; /* 기본 테두리 제거 */
  opacity: 0.5;
  transition: opacity 0.6s ease;
}

.carousel-indicators .active {
  opacity: 1;
}

/* 기존 hero-text-overlay는 Toss 스타일과 맞지 않아 제거 */
/* .hero-text-overlay { ... } */

.features-section,
.latest-articles-section {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 0; /* 전체 화면 섹션이므로 둥근 모서리 제거 */
  box-shadow: none; /* 그림자 제거 */
  margin-bottom: 0; /* 기존 마진 제거 */
  text-align: center;
  justify-content: flex-start; /* 내용을 상단에 정렬 */
  padding-top: 5vh; /* 상단 여백 추가 */
}

.features-section h2,
.latest-articles-section h2 {
  color: #333;
  margin-bottom: 1.5rem;
  font-size: 2.5rem; /* 제목 크기 키움 */
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* 아이템 크기 조정 */
  gap: 2rem; /* 간격 조정 */
  margin-top: 1.5rem;
  max-width: 1200px; /* 최대 너비 설정 */
  width: 90%; /* 반응형 너비 */
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem; /* 패딩 조정 */
  border: none; /* 테두리 제거 */
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: #f8f9fa; /* 배경색 추가 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* 그림자 추가 */
}

.feature-item:hover {
  transform: translateY(-8px); /* 호버 효과 강화 */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* 호버 그림자 강화 */
}

.feature-icon {
  width: 80px; /* 아이콘 크기 키움 */
  height: 80px;
  margin-bottom: 1.2rem;
  object-fit: contain;
}

.feature-item h3 {
  font-size: 1.5rem; /* 제목 크기 키움 */
  color: #43B883;
  margin-bottom: 0.8rem;
}

.feature-item p {
  font-size: 1rem; /* 텍스트 크기 키움 */
  color: #666;
  text-align: center;
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* 아이템 크기 조정 */
  gap: 2rem; /* 간격 조정 */
  margin-top: 1.5rem;
  max-width: 1200px; /* 최대 너비 설정 */
  width: 90%; /* 반응형 너비 */
}

.article-card {
  background-color: #f8f9fa;
  padding: 2rem; /* 패딩 조정 */
  border-radius: 8px;
  text-align: left;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* 그림자 추가 */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.article-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.article-card h3 {
  font-size: 1.3rem; /* 제목 크기 키움 */
  color: #333;
  margin-bottom: 0.8rem;
}

.article-card p {
  font-size: 0.95rem; /* 텍스트 크기 키움 */
  color: #777;
  margin-bottom: 1.2rem;
}

.read-more {
  color: #43B883;
  text-decoration: none;
  font-weight: bold;
  font-size: 1rem; /* 텍스트 크기 키움 */
}

.read-more:hover {
  text-decoration: underline;
}

.app-footer {
  background-color: #43B883;
  color: white;
  padding: 2rem 1rem;
  text-align: center;
  width: 100%;
  margin-top: 0; /* 기존 마진 제거 */
}

.footer-content p {
  margin: 0.5rem 0;
  font-size: 1rem; /* 텍스트 크기 키움 */
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .features-section h2,
  .latest-articles-section h2 {
    font-size: 2.2rem;
  }
  .feature-icon {
    width: 70px;
    height: 70px;
  }
  .feature-item h3 {
    font-size: 1.3rem;
  }
  .feature-item p {
    font-size: 0.9rem;
  }
  .article-card h3 {
    font-size: 1.2rem;
  }
  .article-card p {
    font-size: 0.9rem;
  }
}

@media (max-width: 768px) {
  .features-section h2,
  .latest-articles-section h2 {
    font-size: 2rem;
  }
  .features-grid,
  .articles-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    width: 95%;
  }
  .feature-icon {
    width: 60px;
    height: 60px;
  }
  .feature-item h3 {
    font-size: 1.2rem;
  }
  .feature-item p {
    font-size: 0.85rem;
  }
  .article-card h3 {
    font-size: 1.1rem;
  }
  .article-card p {
    font-size: 0.8rem;
  }
  .app-footer {
    padding: 1.5rem 0.5rem;
  }
}

@media (max-width: 480px) {
  .features-section h2,
  .latest-articles-section h2 {
    font-size: 1.8rem;
  }
  .features-grid,
  .articles-grid {
    grid-template-columns: 1fr; /* Stack items on very small screens */
    width: 95%;
  }
  .feature-icon {
    width: 50px;
    height: 50px;
  }
  .feature-item h3 {
    font-size: 1.1rem;
  }
  .feature-item p {
    font-size: 0.8rem;
  }
  .article-card h3 {
    font-size: 1rem;
  }
  .article-card p {
    font-size: 0.75rem;
  }
  .app-footer {
    padding: 1rem 0.5rem;
  }
}
</style>
