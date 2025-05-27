<template>
  <div>
    <div class="card">
      <img
        :src="video.snippet.thumbnails.high.url"
        class="card-img-top"
        alt="..."
      />
      <div class="card-body">
        <h5 class="card-title">{{ decodeHTMLEntities(video?.snippet.title) }}</h5>
        <button
          @click="onClick"
          class="card-link"
          style="
            background: none;
            border: none;
            padding: 0;
            color: blue;
            text-decoration: underline;
            cursor: pointer;
          "
        >
          +더보기
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const props = defineProps({
  video: Object,
})

const router = useRouter()

function onClick() {
  console.log('버튼클릭')
  router.push({ name: 'search-detail', params: { id: props.video?.id?.videoId } })
}

function decodeHTMLEntities(text) {
  const textarea = document.createElement('textarea')
  textarea.innerHTML = text
  return textarea.value
}
</script>

<style scoped>
.card {
  width: 100%;
  height: 320px; /* ✅ 전체 높이 고정 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
  border-radius: 8px;
  overflow: hidden;
}

.card-img-top {
  object-fit: cover;
  height: 160px;
  width: 100%;
}

.card-body {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
}

.card-title {
  font-size: 1rem;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
