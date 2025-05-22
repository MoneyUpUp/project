<template>
  <div class="item">
    <div class="left">
      <img src="" alt="은행로고" />
      <div class="info">
        <h4>Sh첫만남우대예금</h4>
        <p>Sh수협은행 · 누구나가입</p>
        <span class="tag">방문없이가입</span>
      </div>
    </div>
    <div class="right">
      <p class="rate">최고 <strong>3.10%</strong></p>
      <p class="base">기본 2.05%</p>
    </div>
  </div>
</template>

<script setup>
// props 처리 필요시 확장 가능
</script>

<style scoped>
.item {
  background: white;
  border-radius: 16px;
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.left {
  display: flex;
  gap: 12px;
  align-items: center;
}

.left img {
  width: 40px;
  height: 40px;
}

.info h4 {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
}

.info p {
  margin: 0;
  font-size: 14px;
  color: #444;
}

.tag {
  font-size: 12px;
  background-color: #eee;
  padding: 2px 6px;
  border-radius: 4px;
  display: inline-block;
  margin-top: 4px;
}

.right {
  text-align: right;
}

.rate {
  color: #2eb474;
  font-weight: 600;
}

.base {
  font-size: 13px;
  color: #aaa;
}
</style>
