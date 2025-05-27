<template>
  <div>
    <hr style="margin: 5px auto" />
    <table class="table">
      <thead>
        <tr>
          <th
            scope="col"
            class="tableSt"
            style="width: 5%"
          >
            <input
              type="checkbox"
              :checked="allSelected"
              @change="toggleAll"
            />
          </th>
          <th style="width: 10%">은행</th>
          <th
            scope="col"
            style="width: 30%"
          >
            예 적금 명
          </th>
          <th
            scope="col"
            class="tableSt"
            style="width: 5%"
          >
            종류
          </th>
          <th
            scope="col"
            class="tableSt"
            style="width: 20%"
          >
            가입대상
          </th>
          <th
            scope="col"
            class="tableSt"
            style="width: 20%"
          >
            가입방법
          </th>
        </tr>
      </thead>
      <tbody>
        <!-- 예금 리스트 -->
        <template v-if="items.favorite_deposits?.length">
          <AccessionListItem
            v-for="item in items.favorite_deposits"
            :key="`deposit-${item.bank.fin_co_no}-${item.fin_prdt_cd}`"
            :item="{ ...item, type: 'deposit' }"
            :is-selected="isSelected(item)"
            @update:selected="updateSelection(item, $event)"
          />
        </template>

        <!-- 적금 리스트 -->
        <template v-if="items.favorite_savings?.length">
          <AccessionListItem
            v-for="item in items.favorite_savings"
            :key="`saving-${item.bank.fin_co_no}-${item.fin_prdt_cd}`"
            :item="{ ...item, type: 'saving' }"
            :is-selected="isSelected(item)"
            @update:selected="updateSelection(item, $event)"
          />
        </template>

        <!-- 자산 리스트 -->
        <template v-if="items.favorite_assets?.length">
          <AccessionListItem
            v-for="item in items.favorite_assets"
            :key="`asset-${item.bank?.fin_co_no || 'none'}-${item.fin_prdt_cd}`"
            :item="{ ...item, type: 'asset' }"
            :is-selected="isSelected(item)"
            @update:selected="updateSelection(item, $event)"
          />
        </template>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import AccessionListItem from './AccessionListItem.vue'

const props = defineProps({
  items: Object,
})

const emit = defineEmits(['update:selected-items'])

const selectedItems = ref([])

const allItems = computed(() => {
  const deposits = props.items.favorite_deposits || []
  const savings = props.items.favorite_savings || []
  const assets = props.items.favorite_assets || []
  console.log('AccessionList - allItems computed:', [...deposits, ...savings, ...assets])
  return [...deposits, ...savings, ...assets]
})

const allSelected = computed({
  get: () => selectedItems.value.length === allItems.value.length && allItems.value.length > 0,
  set: (value) => {
    if (value) {
      selectedItems.value = [...allItems.value]
    } else {
      selectedItems.value = []
    }
    console.log('AccessionList - allSelected set:', selectedItems.value)
  },
})

const isSelected = (item) => {
  const result = selectedItems.value.some(
    (selected) =>
      selected.fin_prdt_cd === item.fin_prdt_cd &&
      selected.type === item.type &&
      selected.bank?.fin_co_no === item.bank?.fin_co_no,
  )
  return result
}

const updateSelection = (item, isChecked) => {
  if (isChecked) {
    selectedItems.value.push(item)
  } else {
    selectedItems.value = selectedItems.value.filter(
      (selected) =>
        !(
          selected.fin_prdt_cd === item.fin_prdt_cd &&
          selected.type === item.type &&
          selected.bank?.fin_co_no === item.bank?.fin_co_no
        ),
    )
  }
  console.log('AccessionList - selectedItems after updateSelection:', selectedItems.value)
}

const toggleAll = (event) => {
  allSelected.value = event.target.checked
}

watch(
  selectedItems,
  (newVal) => {
    console.log('AccessionList - selectedItems changed, emitting:', newVal)
    emit('update:selected-items', newVal)
  },
  { deep: true },
)

watch(
  () => props.items,
  (newVal) => {
    console.log('AccessionList - props.items changed:', newVal)
    selectedItems.value = selectedItems.value.filter((selected) =>
      allItems.value.some(
        (item) =>
          item.fin_prdt_cd === selected.fin_prdt_cd &&
          item.type === selected.type &&
          item.bank?.fin_co_no === selected.bank?.fin_co_no,
      ),
    )
    console.log(
      'AccessionList - selectedItems after props.items change filter:',
      selectedItems.value,
    )
  },
  { deep: true },
)
</script>

<style lang="scss" scoped>
@use '@/assets/styles/utils/variables' as *;

.tableSt {
  text-align: center;
}
</style>
