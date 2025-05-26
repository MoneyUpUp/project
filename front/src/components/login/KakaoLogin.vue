<template>
  <div>
    <a
      v-if="!user.email"
      @click.prevent="kakaoLogin"
    >
      <img
        src="//k.kakaocdn.net/14/dn/btqCn0WEmI3/nijroPfbpCa4at5EIsjyf0/o.jpg"
        width="222"
      />
    </a>
    <div v-else>
      <p>nickname: {{ user.name }}</p>
      <p>email: {{ user.email }}</p>
      <button
        type="button"
        @click="kakaoLogout"
      >
        카카오 로그아웃
      </button>
    </div>
    </div>
  </template>
  
<script>
import { loadScript, removeScript } from "@/utils/kakao/useKakaoScript";
import { onMounted, onBeforeUnmount } from "vue";
import { useAccountStore } from "@/stores/accounts";
// import { useRouter } from "vue-router"; // Removed as we'll use this.$router

const key = import.meta.env.VITE_KAKA_API_KEY;
const jskey = import.meta.env.VITE_KAKAO_API_JS_KEY;

export default {
  name: "KakaoLogin",
  data() {
    return {
      user: {},
    };
  },
  async mounted() {
    await loadScript({
      id: "kakao-sdk",
      src: "https://developers.kakao.com/sdk/js/kakao.js",
      onLoad: () => {
        if (!window.Kakao?.isInitialized?.()) {
          window.Kakao.init(jskey);
          console.log("✅ Kakao SDK initialized");
        }
      },
    });

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has("code")) {
      const code = urlParams.get("code");
      await this.setKakaoToken(code);
    }
  },
  beforeUnmount() {
    removeScript("kakao-sdk");
    if (window.Kakao) {
      delete window.Kakao;
    }
  },
  methods: {
    kakaoLogin() {
       console.log("🔑 카카오 로그인 시작");

      if (!window.Kakao || !window.Kakao.Auth) {
        console.error("⚠️ Kakao SDK가 로드되지 않았습니다.");
        return;
      }
      window.Kakao.Auth.authorize({
        redirectUri: "http://localhost:5173/login/kakao",
      });
    },
    async setKakaoToken(code) {
      const store = useAccountStore();

      const result = await fetchKakaoToken(code);
      if (result?.data?.access_token) {
        const accessToken = result.data.access_token;
        
        window.Kakao.Auth.setAccessToken(result.data.access_token);
        await this.setUserInfo();

        try {
          const response = await axios.post("http://127.0.0.1:8000/auth/kakao/login/", {
            access_token: accessToken,
          }, {
            headers: {
              "Content-Type": "application/json",
            },
          });

          console.log("✅ 백엔드 응답:", response.data);
          store.setToken(response.data.token); // Use the action
          this.$router.push({name: 'home'}); // Use this.$router
        } catch (error) {
          console.error("❌ Error during backend request or subsequent operations:", error);
        }
      }
    },
    async setUserInfo() {
      const userData = await fetchKakaoUser();
      this.user = {
        name: userData.kakao_account.profile.nickname,
        email: userData.kakao_account.email,
      };
    },
    kakaoLogout() {
      this.user = {};
      window.Kakao.Auth.logout().then(() => {
        console.log("로그아웃 성공");
      });
    },
  },
};

// 별도 함수 (컴포넌트 바깥)
import axios from "axios";
const KAKAO_API_KEY = import.meta.env.VITE_KAKAO_API_KEY;

async function fetchKakaoToken(code) {
  const data = {
    grant_type: "authorization_code",
    client_id: KAKAO_API_KEY,
    redirect_uri: "http://localhost:5173/login/kakao",
    code,
  };

  const queryString = Object.keys(data)
    .map((k) => `${encodeURIComponent(k)}=${encodeURIComponent(data[k])}`)
    .join("&");

  const response = await axios.post(
    "https://kauth.kakao.com/oauth/token",
    queryString,
    {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
      },
    }
  );
  return response;
}

async function fetchKakaoUser() {
  try {
    const res = await window.Kakao.API.request({ url: "/v2/user/me" });
    return res;
  } catch (err) {
    console.error("유저 정보 요청 실패", err);
    return {};
  }
}
</script>
