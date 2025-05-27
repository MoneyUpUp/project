import json
from openai import OpenAI
from django.conf import settings
import os


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_reasons_from_gpt(user, product_options):
    print(product_options)
    invest_type_display = user.get_invest_type_display()
    preferred_term_display = user.get_preferred_term_display()

    # 상품 리스트를 GPT에 보여줄 형태로 만듦
    product_descriptions = "\n".join(
        [
            f"{i+1}. [{opt['type']}] {opt['name']} - {opt['bank']} ({opt['save_trm']}개월, 금리 {opt['interest_rate']}%)"
            for i, opt in enumerate(product_options)
        ]
    )

    prompt = f"""
    사용자 정보:
    - 투자 성향: {invest_type_display}
    - 희망 투자 기간: {preferred_term_display}

    다음은 추천할 금융 상품 목록입니다:

    {product_descriptions}

    각 상품에 대해, **이유(reason)**만 JSON 배열로 생성해줘.
    형식은 다음과 같아야 해:

    [
      {{
        "reason": "이 상품은 안정적이면서 금리가 높아 투자 성향에 적합합니다."
      }},
      ...
    ]

    ✨ 총 {len(product_options)}개의 이유를, 순서대로 정확히 배열로 반환해줘.
    다른 설명이나 문자열은 붙이지 말고, JSON만 출력해.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 금융 상품 추천 전문가야."},
            {"role": "user", "content": prompt},
        ],
        temperature=1,
        max_tokens=512,
    )

    try:
        gpt_reasons = json.loads(response.choices[0].message.content)

        # product_options와 이유를 묶어서 반환
        combined = []
        for opt, reason_data in zip(product_options, gpt_reasons):
            combined.append(
                {
                    "type": opt["type"],
                    "id": opt["id"],
                    "bank": opt["bank"],
                    "bank_id": opt["bank_id"],
                    "reason": reason_data["reason"],
                }
            )
        return combined

    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print("GPT 응답 파싱 오류:", e)
        return []
