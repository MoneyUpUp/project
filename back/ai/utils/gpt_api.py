import json
from openai import OpenAI
from django.conf import settings
import os


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_reasons_from_gpt(user, product_options):
    invest_type_display = user.get_invest_type_display()
    preferred_term_display = user.get_preferred_term_display()
    print(f"✅ settings.OPENAI_API_KEY: {settings.OPENAI_API_KEY}")
    # OPENAI_API_KEY = "..."
    # client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
    사용자 정보:
    - 투자 성향: {invest_type_display}
    - 희망 투자 기간: {preferred_term_display}


    각 상품에 대해 사용자에게 적합한 이유를 설명해줘.

    JSON 배열 형식으로 응답해야 하며, 각 항목에는 반드시 아래와 같은 키가 포함되어야 합니다:

    - type: "deposit" 또는 "saving" (상품 종류)
    - id: 상품 ID (정수형)
    - reason: 사용자에게 왜 이 상품이 적합한지 설명하는 한 문장

    다음 형식처럼 정확히 출력해 주세요:

    [
    {{
        "type": "deposit",
        "id": 1,
        "reason": "이 상품은 금리가 높고, 사용자 성향에 적합하여 추천됩니다."
    }},
    ...
    ]

    ※ 응답은 JSON 배열 자체로만 출력하고, 문자열로 감싸지 마세요.
    """

    # chat.completions API 사용 (최신 방식)
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 또는 fallback 확인 중이면 "gpt-4o-mini"
        messages=[
            {"role": "system", "content": "너는 금융 상품 추천 전문가야."},
            {"role": "user", "content": prompt},
        ],
        temperature=1,
        max_tokens=256,
    )

    # 응답 추출 방식 업데이트
    return json.loads(response.choices[0].message.content)
