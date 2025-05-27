<template>
  <div class="article-detail-container">
    <header class="header">
      <h1 class="title">{{ article.title }}</h1>
      <div class="meta">
        <span>작성자: {{ article.author }}</span>
        <span>작성일: {{ article.date }}</span>
        <span>조회수: {{ article.views }}</span>
      </div>
    </header>

    <section class="content">
      <p v-for="(paragraph, index) in article.content.split('\n')" :key="index">
        {{ paragraph }}
      </p>
    </section>

    <div class="actions">
      <button class="btn primary" @click="goToUpdatePage" >수정</button>
      <button class="btn danger" @click="deleteArticle">삭제</button>
    </div>

    <section class="comments">
      <h2>댓글</h2>
      <div v-if="comments.length === 0" class="no-comments">
        아직 댓글이 없습니다.
      </div>
      <div class="comment" v-for="comment in comments" :key="comment.id">
        <div class="comment-meta">
          <strong>{{ comment.author }}</strong>
          <span>{{ comment.date }}</span>
        </div>
        <p>{{ comment.text }}</p>
      </div>

      <div class="comment-form">
        <h3>댓글 작성</h3>
        <textarea placeholder="댓글을 입력하세요" v-model="newComment"></textarea>
        <button class="btn success">작성하기</button>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/Articles'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const articleStore = useArticleStore()

const article = ref({
  title: '로딩 중...',
  author: '',
  date: '',
  views: 0,
  content: '게시글 내용을 불러오는 중입니다.',
})

const comments = ref([])
const newComment = ref('')

onMounted(async () => {
  const articleId = route.params.articleId
  if (articleId) {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/community/articles/${articleId}/`)
      article.value = response.data
      comments.value = response.data.comments || []
    } catch (error) {
      console.error('게시글 불러오기 실패:', error)
      article.value.title = '게시글을 불러올 수 없습니다.'
    }
  }
})

const goToUpdatePage = () => {
  const articleId = route.params.articleId
  router.push({ name: 'article-update', params: { articleId } })
}

const deleteArticle = async () => {
  const articleId = route.params.articleId
  try {
    await axios.delete(`http://127.0.0.1:8000/community/articles/${articleId}/`,
		{
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`,
        },
      }
		)
    alert('삭제되었습니다.')
		articleStore.routeCommunity()
		router.push({ name: 'articleList' })
  } catch (error) {
    console.error('삭제 실패:', error)
    alert('삭제 중 오류 발생')
  }
}
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

.article-detail-container {
  max-width: 880px;
  margin: $space-xl auto;
  padding: $space-xl;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  font-family: $font-base;
  color: $gray-800;
  font-size: 1.05rem;
}

.header {
  margin-bottom: $space-xl;

  .title {
    font-size: 2.25rem;
    color: $primary-700;
    margin-bottom: $space-sm;
    font-weight: bold;
  }

  .meta {
    font-size: 0.95rem;
    color: $gray-600;
    display: flex;
    gap: $space-lg;
  }
}

.content {
  line-height: 1.9;
  margin-bottom: $space-xl;

  p {
    margin-bottom: $space-md;
  }
}

.actions {
  display: flex;
  justify-content: flex-end;
  gap: $space-sm;
  margin-bottom: $space-xl;

  .btn {
    padding: 12px 24px;
    border-radius: 999px;
    font-weight: bold;
    cursor: pointer;
    border: none;
    font-size: 1rem;

    &.primary {
      background: $primary-500;
      color: white;

      &:hover {
        background: $primary-600;
      }
    }

    &.danger {
      background: $red-500;
      color: white;

      &:hover {
        background: $red-600;
      }
    }
  }
}

.comments {
  border-top: 1px solid $gray-200;
  padding-top: $space-lg;

  h2 {
    font-size: 1.6rem;
    color: $primary-700;
    margin-bottom: $space-md;
  }

  .comment {
    background: $gray-50;
    border: 1px solid $gray-100;
    border-radius: 10px;
    padding: $space-md;
    margin-bottom: $space-md;

    .comment-meta {
      font-size: 0.9rem;
      color: $gray-600;
      margin-bottom: $space-xs;

      strong {
        color: $primary-600;
        margin-right: $space-sm;
      }
    }

    p {
      margin: 0;
      color: $gray-800;
    }
  }

  .no-comments {
    font-size: 0.95rem;
    color: $gray-500;
    margin-bottom: $space-md;
  }

  .comment-form {
    margin-top: $space-lg;

    h3 {
      font-size: 1.25rem;
      color: $primary-600;
      margin-bottom: $space-sm;
    }

    textarea {
      width: 100%;
      border: 1px solid $gray-300;
      border-radius: 8px;
      padding: $space-md;
      margin-bottom: $space-md;
      font-family: $font-base;
      resize: vertical;
      min-height: 100px;
    }

    .btn.success {
      background: $green-500;
      color: white;
      padding: 10px 24px;
      border-radius: 999px;
      font-weight: bold;
      font-size: 1rem;

      &:hover {
        background: $green-600;
      }
    }
  }
}
</style>
