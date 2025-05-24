export const BANKS_BY_ID = {
  '0010927': { name: 'KB국민', slug: 'kb-bank' },
  '0011625': { name: '신한', slug: 'shinhan-bank' },
  '0013909': { name: '하나', slug: 'hana-bank' },
  '0010001': { name: '우리', slug: 'woori-bank' },
  '0013175': { name: 'NH농협', slug: 'nh-bank' },
  '0010002': { name: 'SC제일', slug: 'sc-bank' },
  '0010017': { name: '부산', slug: 'bnk-bank' },
  '0010024': { name: '경남', slug: 'bnk-bank' },
  '0010016': { name: 'iM뱅크', slug: 'im-bank' },
  '0014807': { name: 'SH수협', slug: 'sh-bank' },
  '0015130': { name: '카카오뱅크', slug: 'kakao-bank' },
  '0010019': { name: '광주', slug: 'jb-bank' },
  '0010022': { name: '전북', slug: 'jb-bank' },
  '0017801': { name: '토스뱅크', slug: 'toss-bank' },
  '0014674': { name: '케이뱅크', slug: 'k-bank' },
  '0010020': { name: '제주', slug: 'shinhan-bank' },
  '0010026': { name: 'IBK기업', slug: 'ibk-bank' },
  '0010030': { name: 'KDB산업', slug: 'kdb-bank' },
}

// 드롭다운용 옵션 리스트
export const BANK_OPTIONS = [
  { label: '전체 은행', value: 'all' },
  ...Object.entries(BANKS_BY_ID).map(([id, { name }]) => ({
    value: id,
    label: name,
  })),
]

// 로고 경로 반환
export function getBankLogoById(bankId) {
  const slug = BANKS_BY_ID[bankId]?.slug

  if (!slug) {
    console.warn(`❗️로고를 찾을 수 없음: ID ${bankId}`)
    return new URL('../assets/images/banks/default.png', import.meta.url).href
  }

  return new URL(`../assets/images/banks/${slug}.png`, import.meta.url).href
}
