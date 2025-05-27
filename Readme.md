# 🌱 MoneyUp - 당신의 금융을 한눈에!

> 예·적금 비교부터 AI 추천, 커뮤니티까지!
> Vue + Django 기반의 **종합 금융 플랫폼**입니다 💸

---

## 📁 프로젝트 구조

```
MoneyUp/
├── back/          # Django 백엔드
│   ├── accounts/       👤 사용자 인증 및 프로필
│   ├── products/       💰 예·적금 상품 관리
│   ├── community/      🗣️ 게시판 & 댓글
│   ├── ai/             🤖 GPT 추천 & 챗봇
│   └── MoneyUp/        ⚙️ Django 설정
├── front/         # Vue.js 프론트엔드
│   ├── components/     🧩 재사용 UI 컴포넌트
│   ├── views/          📄 페이지 단위 화면
│   ├── store/          🧠 상태 관리 (Pinia)
│   └── assets/         🎨 SCSS · 이미지
├── README.md      # 📘 이 문서
├── .gitignore     # 🙈 Git 제외 파일
└── uninstall.txt  # 🧹 초기화 지침
```

---

## 🌟 주요 기능 소개

| 기능             | 설명                                     |
| ---------------- | ---------------------------------------- |
| 💰 예·적금 비교   | 은행별 상품 조건과 최고 이율 한눈에 확인 |
| ❤️ 찜하기         | 관심 있는 금융 상품 즐겨찾기 저장        |
| 🌎 주변 은행 찾기 | Kakao Map 기반 위치 탐색 기능            |
| 💱 환율 계산기    | 실시간 환율 확인 및 환전 금액 계산       |
| 🗣️ 커뮤니티       | 금융 관련 소통 공간 (글 작성, 댓글)      |
| 🧠 AI 추천/챗봇   | GPT 기반 금융 상품 추천 및 금융 상담     |
| 📈 현물 차트      | 금·은·원유 등 원자재 가격 시각화         |

---

## 🛠 기술 스택

**Backend**

* Django, DRF, SQLite
* Swagger (drf-yasg), Simple JWT
* OpenAI GPT API

**Frontend**

* Vue 3, Vite, Pinia, Vue Router
* Axios, SCSS, Pretendard 폰트
* Kakao Maps API

**Workflow & 협업**

* Git + GitHub, Git Flow 브랜치 전략
* RESTful API 문서화
* 커밋 컨벤션: `type: message`

---

## 🚀 설치 가이드

### 1. 레포지토리 클론

```bash
git clone -b develop https://github.com/SunshineMoonGit/MoneyUp.git
```

---

### 2. 백엔드 설정

```bash
cd MoneyUp/back
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env         # 환경 변수 설정
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

### 3. 프론트엔드 설정

```bash
cd ../front
npm install
cp .env.example .env.local
npm run dev
```

➡️ 브라우저에서 `http://localhost:5173` 접속

---


## 📚 API 문서

Swagger UI:
👉 [`http://localhost:8000/swagger/`](http://localhost:8000/swagger/)

---


## 💬 마지막 한 마디

MoneyUp은 **직관적이고, 똑똑하고, 따뜻한 금융 플랫폼**을 목표로 하고 있습니다.
누구나 쉽고 빠르게 금융 정보를 비교하고, 소통하고, 추천받을 수 있는 공간을 만들어가고 있어요.