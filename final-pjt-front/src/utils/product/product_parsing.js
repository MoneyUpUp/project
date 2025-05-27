export function parseProduct(data) {
  return {
    id: data.id,
    bankId: data.bank.fin_co_no,
    bankName: data.bank.kor_co_nm,
    options: data.options,
    dcls_month: data.dcls_month,
    fin_prdt_cd: data.fin_prdt_cd,
    fin_prdt_nm: data.fin_prdt_nm,
    join_way: data.join_way?.split(',') || [],
    mtrt_int: data.mtrt_int,
    spcl_cnd: data.spcl_cnd,
    join_deny: data.join_deny,
    join_member: data.join_member,
    etc_note: data.etc_note,
    max_limit: data.max_limit,
    dcls_strt_day: data.dcls_strt_day,
    dcls_end_day: data.dcls_end_day,
    fin_co_subm_day: data.fin_co_subm_day,
  }
}
