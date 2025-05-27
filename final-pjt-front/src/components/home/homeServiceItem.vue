<!-- homeServiceItem.vue -->
<template>
  <div class="card-wrapper" :style="{ backgroundColor: service.bg }">
    <div class="card-body">
      <h5 class="card-title">{{ service.title }}</h5>
      <p class="card-text">{{ service.content }}</p>
      <a :href="service.path" class="card-link">바로가기</a>
      <p class="card-date">Date</p>
    </div>
  </div>
</template>


<script setup>
defineProps({
    service: Object
})
</script>

<style scoped>
.card-wrapper {
  width: 287px;
  height: 173px;
  border-radius: 8px;
  padding: 16px;
  box-sizing: border-box;
  font-family: 'Pretendard', sans-serif;
  transition: box-shadow 0.5s;
}

.card-wrapper:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 6px;
	/* width: 287px;
  height: 173px; */
}

.card-title {
  font-size: 16px;
  font-weight: 700;
  margin: 0;
  color: #111;
}

.card-text {
  font-size: 14px;
  color: #333;
  margin: 0;
}

.card-link {
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  color: #111;
  margin-top: 8px;
}

.card-date {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.4);
  margin: 0;
}
</style>