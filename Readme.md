# MoneyUp

예·적금 상품 비교, 맞춤형 추천, 금융 AI 챗봇, 커뮤니티 기능을 제공하는 통합 금융 플랫폼입니다.  
프론트엔드는 **Vue 3 + Vite**, 백엔드는 **Django REST Framework** 기반으로 개발되었습니다.

---

## Frontend (Vue 3 + Vite)

### 개발 환경

- **권장 IDE**: [VSCode](https://code.visualstudio.com/)
- **확장 프로그램**: [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
  > ⚠️ 기존 Vetur 확장은 비활성화하세요.

### 프로젝트 설정

1. 의존성 설치
   ```sh
   npm install
   ```
2. 개발 서버 실행
   ```sh
   npm run dev
   ```
3. 프로덕션 빌드
   ```sh
   npm run build
   ```

### 환경 변수 설정

루트 디렉토리에 `.env` 파일을 생성하고 다음 내용을 추가하세요.

```env
VITE_YOUTUBE_API_KEY=your_youtube_api_key
VITE_KAKAO_API_JS_KEY=your_kakao_api_js_key
```

> `.env` 파일은 `.gitignore`에 포함되어 있어 저장소에 올라가지 않습니다.  
> 팀원은 각자 로컬 환경에서 직접 키를 입력해야 합니다.

---

## Backend (Django REST Framework)

### 개발 환경

- Python 3.13.5
- Django 4.2.20
- Django REST Framework
- SQLite3 (개발용 DB)

### 프로젝트 구조

```
backend/
 ├─ accounts/        # 사용자 인증 및 프로필
 ├─ ai/              # AI 추천 및 챗봇
 ├─ community/       # 게시글 및 댓글
 ├─ products/        # 예금/적금 상품
 ├─ swaggers/        # API 문서 (Swagger)
 ├─ final/           # 메인 프로젝트 설정
 ├─ manage.py
 ├─ requirements.txt
 └─ .env
```

### 환경 변수 설정

루트 디렉토리에 `.env` 파일을 생성하고 다음 내용을 설정하세요.

```env
# 소셜 로그인
KAKAO_CLIENT_ID=your-kakao-client-id
KAKAO_SECRET=your-kakao-secret

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_SECRET=your-google-secret

NAVER_CLIENT_ID=your-naver-client-id
NAVER_SECRET=your-naver-secret

# 외부 API 키
FIN_API_KEY=your-finance-api-key
OPENAI_API_KEY=your-openai-api-key
```

> `.env` 파일은 `.gitignore`에 포함되어 있어 저장소에 올라가지 않습니다.  
> 팀원은 각자 로컬 환경에서 직접 키를 입력해야 합니다.

### 실행 방법

1. 가상환경 생성 및 활성화
   ```bash
   python -m venv .venv
   ```
   ```bash
   source .venv/bin/activate   # Mac/Linux
   source .venv\Scripts\activate    # Windows
   ```
2. 의존성 설치
   ```bash
   pip install -r requirements.txt
   ```
3. 마이그레이션
   ```bash
   python manage.py migrate
   ```
4. 슈퍼유저 생성
   ```bash
   python manage.py createsuperuser
   ```
5. 서버 실행
   ```bash
   python manage.py runserver
   ```

### API 문서

Swagger UI 제공:  
`http://127.0.0.1:8000/swagger/`

### 데이터 백업 및 복원

- 백업
  ```bash
  python manage.py dumpdata > products_backup.json
  ```
- 복원
  ```bash
  python manage.py loaddata products_backup.json
  ```
