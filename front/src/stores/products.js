import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  async function depositData() {
    console.log('함수호출')
    const res = await fetch('/deposit.json');
    const data = await res.json();
    // console.log(data);
    return data;
  }
  return { depositData }
})
