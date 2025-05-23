<template>
  <BaseSelect
    v-model="mapStore.selectedState"
    :options="mapStore.states"
    placeholder="도/시"
    @change="mapStore.onStateChange"
  />

  <BaseSelect
    v-model="mapStore.selectedCity"
    :options="mapStore.cities"
    placeholder="시/군/구"
  />

  <BaseSelect
    v-model="mapStore.selectedBank"
    :options="mapStore.banks"
    placeholder="은행"
  />

  <BaseButton @click="mapStore.onSearch">검색</BaseButton>
</template>

<script setup>
import BaseSelect from '@/components/base/BaseSelect.vue'
import BaseButton from '@/components/base/BaseButton.vue'

import { useMapStore } from '@/stores/mapStore'

const mapStore = useMapStore()
</script>
