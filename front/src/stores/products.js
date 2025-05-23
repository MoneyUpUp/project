import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  async function depositData() {
    const res = await fetch('/deposit.json');
    const data = await res.json();
    return data;
    // console.log(data);
  }
  return { depositData }
})
