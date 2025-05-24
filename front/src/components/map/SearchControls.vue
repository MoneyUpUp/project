<template>
  <BaseSelect
    v-model="mapStore.selectedState"
    :options="mapStore.states"
    placeholder="도/시"
    @change="mapStore.onStateChange"
    variant="default"
  />

  <BaseSelect
    v-model="mapStore.selectedCity"
    :options="mapStore.cities"
    placeholder="시/군/구"
    variant="default"
  />

  <BaseSelect
    v-model="mapStore.selectedBank"
    :options="mapStore.banks"
    placeholder="은행"
    variant="default"
  />

  <BaseButton @click="mapStore.onSearch">검색</BaseButton>
</template>

<script setup>
import BaseButton from '@/components/base/BaseButton.vue'
import BaseSelect from '@/components/base/BaseSelect.vue'

import { useMapStore } from '@/stores/mapStore'

const mapStore = useMapStore()
</script>
