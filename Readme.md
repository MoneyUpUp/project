# 💸 MoneyUp

> 예·적금 상품 비교부터 금융 AI 챗봇까지! Vue + Django 기반 금융 통합 플랫폼

---

## 📌 프로젝트 소개

**MoneyUp**은 예·적금 상품을 비교하고, 추천받고, 주변 은행을 탐색하고, 금융 커뮤니티와 챗봇까지 제공하는 **올인원 금융 플랫폼**입니다. 사용자의 투자 성향에 따른 맞춤형 추천 기능과 다양한 금융 정보를 제공합니다.

---

## 👥 팀원 및 업무 분담

| 이름       | 역할 및 업무                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- |
| **강태욱** | 백엔드 개발<br/>- Django/DRF API 설계·구현<br/>- DB 모델링 및 마이그레이션<br/>- AI 추천·챗봇 기능 구현                   |
| **이지언** | 프론트엔드 개발<br/>- Vue 3 컴포넌트·페이지 구현<br/>- Pinia 상태 관리<br/>- SCSS 스타일링 및 UI/UX<br/>- Kakao Maps 연동 |

---

## 🏗️ 설계 및 구현

- **클라이언트-서버 구조**: Vue SPA ↔ Django REST API
- **백엔드**
  - 앱 분리: `accounts`, `products`, `community`, `ai`
  - 인증: `dj-rest-auth` + 소셜 로그인
  - 문서화: `drf-yasg` 기반 Swagger UI 제공
- **프론트엔드**
  - Vue 3 + Vite + Pinia
  - Axios를 통한 API 통신
  - 반응형 UI, SCSS 스타일링, Pretendard 폰트 적용

---

## 🛠 기술 스택

### Backend

- Django, DRF, SQLite
- TokenAuthentication, dj-rest-auth, drf-yasg
- OpenAI GPT API

### Frontend

- Vue 3, Vite, Pinia, Vue Router
- Axios, SCSS, Pretendard
- Kakao Maps SDK

---

## 🗂️ 프로젝트 아키텍처

```
[ Vue SPA (Frontend) ]
        ↓ Axios
[ Django REST API ]
├── accounts
├── products
├── community
└── ai
        ↓
     SQLite DB
```

---

## 🧩 ERD (데이터베이스 모델링)

> [ERD 다이어그램 보기](./erd.png)

- User, Product(Deposit/Saving), Option, Article, Comment, AI 등으로 구성
- M:N, 1:N 관계를 활용한 관계형 설계

---

## 🔐 API 키 설정 및 환경변수

### 📦 backend (`/back/.env`)

```env
KAKAO_CLIENT_ID=your-kakao-client-id
KAKAO_SECRET=your-kakao-client-secret

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_SECRET=your-google-client-secret

NAVER_CLIENT_ID=your-naver-client-id
NAVER_SECRET=your-naver-client-secret

FIN_API_KEY=8f9e2f333e552f762cc5ff63ad5c3f92

OPENAI_API_KEY=your-open-api-key
```

### 💻 frontend (`/front/.env`)

```env
VITE_YOUTUBE_API_KEY=your-youtube-api-key
VITE_KAKAO_API_JS_KEY=your-kakao-js-api-key
```

---

## 📑 주요 API 명세

### 🔐 인증 관련 (auth)

| URL                   | METHOD | 설명          | 인증 |
| --------------------- | ------ | ------------- | ---- |
| `/auth/login/`        | POST   | 로그인        | ❌   |
| `/auth/signup/`       | POST   | 회원가입      | ❌   |
| `/auth/google/login/` | POST   | 구글 로그인   | ❌   |
| `/auth/kakao/login/`  | POST   | 카카오 로그인 | ❌   |

---

### 👤 사용자 관련 (accounts)

| URL                       | METHOD | 설명                | 인증 |
| ------------------------- | ------ | ------------------- | ---- |
| `/accounts/me/`           | GET    | 유저 정보 조회      | ✅   |
| `/accounts/me/`           | PATCH  | 유저 정보 일부 수정 | ✅   |
| `/accounts/me/`           | DELETE | 회원 탈퇴           | ✅   |
| `/accounts/me/favorites/` | GET    | 찜한 상품 전체 조회 | ✅   |
| `/accounts/me/favorites/` | POST   | 찜한 상품 추가/해제 | ✅   |
| `/accounts/me/favorites/` | DELETE | 찜한 상품 삭제      | ✅   |

---

### 💰 금융 상품 관련 (products)

| URL                                      | METHOD | 설명                     | 인증 |
| ---------------------------------------- | ------ | ------------------------ | ---- |
| `/products/`                             | GET    | 예금 및 적금 전체 조회   | ❌   |
| `/products/spotAssets/{commodity_name}/` | GET    | 현물 자산 과거 가격 조회 | ❌   |

---

### 📝 커뮤니티 (community)

| URL                                          | METHOD | 설명             | 인증 |
| -------------------------------------------- | ------ | ---------------- | ---- |
| `/community/articles/`                       | GET    | 게시글 목록 조회 | ✅   |
| `/community/articles/`                       | POST   | 게시글 작성      | ✅   |
| `/community/articles/{article_id}/`          | GET    | 게시글 상세 조회 | ✅   |
| `/community/articles/{article_id}/`          | PATCH  | 게시글 일부 수정 | ✅   |
| `/community/articles/{article_id}/`          | DELETE | 게시글 삭제      | ✅   |
| `/community/articles/{article_id}/comments/` | GET    | 댓글 목록 조회   | ✅   |
| `/community/comments/{comment_id}/`          | POST   | 댓글 작성        | ✅   |
| `/community/comments/{comment_id}/`          | PUT    | 댓글 전체 수정   | ✅   |
| `/community/comments/{comment_id}/`          | PATCH  | 댓글 일부 수정   | ✅   |
| `/community/comments/{comment_id}/`          | DELETE | 댓글 삭제        | ✅   |

---

### 🤖 생성형 AI 기능 (ai)

| URL                    | METHOD | 설명                    | 인증 |
| ---------------------- | ------ | ----------------------- | ---- |
| `/ai/recommendations/` | GET    | GPT 기반 금융 상품 추천 | ✅   |
| `/ai/chat/{style}/`    | POST   | 스타일별 챗봇 대화 요청 | ✅   |

---

### 📚 기타

| URL         | METHOD | 설명            | 인증 |
| ----------- | ------ | --------------- | ---- |
| `/swagger/` | GET    | Swagger 문서 UI | ❌   |

---

## 🌟 주요 기능

- **예·적금 비교**: 다양한 금융 상품 비교 및 조건 필터링
- **찜하기 기능**: 관심 상품 저장 및 삭제
- **금융 커뮤니티**: 게시글 작성 및 댓글을 통한 정보 교류
- **은행 위치 찾기**: Kakao 지도 기반 주변 은행 탐색
- **원자재 시세 조회**: 금·은·원유 등 실시간 시세 차트 제공
- **AI 추천**: 사용자의 투자 성향을 고려한 맞춤형 상품 추천
- **AI 챗봇**: 다양한 스타일의 챗봇과 금융 상담 가능

---

## 🤖 생성형 AI 활용

- **추천 기능**: 투자 성향과 선호 기간 기반 GPT를 통해 추천 이유 생성
- **챗봇**: 다양한 캐릭터 스타일(system prompt) 기반 챗봇 구현  
  예: 기본 챗봇, 하이텐션 아이돌, 중2병 천재, 욕쟁이 할머니 등

---

## 💬 프로젝트 후기

- Git Flow 전략을 통해 팀원 간의 원활한 협업이 가능했습니다.
- Django 및 Vue를 활용하며 실제 서비스를 만드는 과정에서 다양한 문제 해결 경험을 얻었습니다.
- 특히 소셜 로그인, 챗봇 통합, 지도 API 연동 등 기술적 난이도가 있는 기능들을 직접 구현하면서 큰 성장을 이루었습니다.
- 앞으로는 CI/CD 구성, 성능 최적화, 테스트 코드 작성을 통한 품질 개선이 목표입니다.
