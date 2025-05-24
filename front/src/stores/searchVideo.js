import { ref, computed } from "vue";
import { defineStore } from "pinia";
const key = import.meta.env.VITE_YOUTUBE_API_KEY;

export const useSearchStore = defineStore('search', () => {

    const videoList = ref([])

    const searchCompany = async (keyword) => {
        if (!keyword) return

        try {
            const res = await fetch(
                `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=10&q=${encodeURIComponent(keyword)}&key=${key}`
            )

            const data = await res.json()
            console.log(data)

            if (data.items && Array.isArray(data.items)) {
              videoList.value = data.items.filter(
                (item) => item.id.kind === "youtube#video"
              );
            } else {
              console.error("검색 결과 없음", data);
            }
        } catch (error) {
            console.error("YouTube API 호출 에러: ", error)
        }

    }
    const showDetail = function(id) {
        return videoList.value.find((v) => {
            return v.id?.videoId === id;
        }) || null;
    }

    return {
      videoList,
      searchCompany,
      showDetail,
    };
})