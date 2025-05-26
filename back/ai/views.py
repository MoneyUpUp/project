from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import status

from .utils.gpt_chat_bot import get_chatbot_response
from products.models import DepositOption, SavingOption
from .utils.gpt_api import generate_reasons_from_gpt
from swaggers.ai_swaggers import recommend_products_swagger, chat_bot_swagger


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@recommend_products_swagger
def recommend_products_view(request):
    user = request.user

    term_map = {
        "S": range(1, 6),
        "M": range(6, 13),
        "L": range(12, 100),
    }
    term_range = term_map.get(user.preferred_term, range(1, 100))

    # 예/적금 상품 top 3~5개 가져오기
    deposit_options = (
        DepositOption.objects.filter(save_trm__in=term_range)
        .select_related("product", "product__bank")
        .order_by("-intr_rate2")[:3]
    )

    saving_options = (
        SavingOption.objects.filter(save_trm__in=term_range)
        .select_related("product", "product__bank")
        .order_by("-intr_rate2")[:2]
    )

    # 추천 대상 상품 (총 5개)
    top_options = list(deposit_options) + list(saving_options)

    # GPT에 넘길 요약 정보 준비
    products = [
        {
            "name": opt.product.fin_prdt_nm,
            "bank": opt.product.bank.kor_co_nm,
            "save_trm": opt.save_trm,
            "interest_rate": str(opt.intr_rate2),
        }
        for opt in top_options
    ]

    # GPT로 추천 이유 생성
    recommendations = generate_reasons_from_gpt(user, products)

    return Response({"recommendations": recommendations})


@api_view(["POST"])
@chat_bot_swagger
def chat_bot_view(request, style):
    message = request.data.get("message")
    if not message:
        return Response({"error": "메시지를 입력해주세요."}, status=400)

    answer = get_chatbot_response(message, style=style)
    return Response({"answer": answer})
