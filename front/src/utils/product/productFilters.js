import { BANKS_BY_ID, getBankLogoById } from '@/constants/banks'

export function matchesBank(item, selectedBankId) {
  return selectedBankId === 'all' || item.bank.fin_co_no === selectedBankId
}

export function matchesType(item, selectedTypes) {
  return selectedTypes.includes(item.type)
}

export function matchesPeriod(item, selectedIndex) {
  return selectedIndex === 0 || item.save_trm === selectedIndex * 6
}

export function parseProductData(data, type) {
  return data.map((product) => {
    product.type = type
    product.join_way = product.join_way?.split(',') || []
    const matched = BANKS_BY_ID[product.bank.fin_co_no]
    if (matched) {
      product.bank.logo = getBankLogoById(product.bank.fin_co_no)
      product.bank.kor_co_nm = matched.name
    }
    return product
  })
}
