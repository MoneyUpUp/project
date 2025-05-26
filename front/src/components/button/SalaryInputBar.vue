<template>
    <div>
        <form role="search" style="display: flex;">
        <div class="salary-bar">
          <input type="text" id="salaryUser" class="salaryInput" value="">
        </div>
        <UpdateButton class="salary-update-button"/>
        </form>
    </div>
    </template>
    
    <script setup>
    import UpdateButton from './UpdateButton.vue';
    </script>
    
    <style lang="scss" scoped>
    @use '@/assets/styles/utils/variables' as *; // Corrected path
    
    .salary-bar {
      display: flex;
      flex-direction: row;
      align-items: center;
      padding: 0px;
      gap: 4px;
    
      position: relative;
      width: 330px;
      max-width: 720px;
      height: 46px;
    
      background: #ffffff;
      border-radius: 28px;
      padding: 0 16px; /* 내부 여백 추가 */
      box-sizing: border-box;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
    
    .salary-bar input[type="search"] {
      flex-grow: 1;
      border: none;
      background: transparent;
      outline: none;
      font-size: 16px;
      color: #333;
    }
    
    .salary-bar
    .salary-bar .salary-btn {
      background: none;
      border: none;
      cursor: pointer;
    }

    .salary-update-button {
      margin-left: 20px;
    }
    
  
    
    
    </style>
