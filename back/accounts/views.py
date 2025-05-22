# accounts/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class AuthCheckView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="현재 로그인된 사용자인지 확인합니다.",
        responses={200: openapi.Response("성공", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'is_authenticated': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                'user': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ))}
    )
    def get(self, request):
        return Response({
            "is_authenticated": True,
            "user": request.user.username
        })
