from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from community.serializers import ArticleSerializer, CommentSerializer

TAG = ["community"]
# ----- ArticleView -----
article_list_get = swagger_auto_schema(
    operation_summary="게시글 전체 목록 조회",
    operation_description="모든 게시글을 생성일 기준 내림차순으로 조회합니다.",
    responses={200: ArticleSerializer(many=True)},
    tags=TAG,
)

article_create_post = swagger_auto_schema(
    operation_summary="게시글 작성",
    operation_description="사용자가 새로운 게시글을 작성합니다.",
    request_body=ArticleSerializer,
    responses={201: ArticleSerializer, 400: "유효성 검사 실패"},
    tags=TAG,
)


# ----- ArticleDetailView -----
article_detail_get = swagger_auto_schema(
    operation_summary="게시글 상세 조회",
    operation_description="특정 게시글의 상세 정보를 조회합니다.",
    responses={200: ArticleSerializer, 404: "존재하지 않는 게시글"},
    tags=TAG,
)

article_update_put = swagger_auto_schema(
    operation_summary="게시글 수정 (전체)",
    operation_description="작성자만 게시글을 전체 수정할 수 있습니다.",
    request_body=ArticleSerializer,
    responses={200: ArticleSerializer, 403: "권한 없음", 400: "유효성 검사 실패"},
    tags=TAG,
)

article_update_patch = swagger_auto_schema(
    operation_summary="게시글 수정 (일부)",
    operation_description="작성자만 게시글을 일부 수정할 수 있습니다.",
    request_body=ArticleSerializer,
    responses={200: ArticleSerializer, 403: "권한 없음", 400: "유효성 검사 실패"},
    tags=TAG,
)

article_delete = swagger_auto_schema(
    operation_summary="게시글 삭제",
    operation_description="작성자만 게시글을 삭제할 수 있습니다.",
    responses={204: "삭제 완료", 403: "권한 없음"},
    tags=TAG,
)


# ----- CommentListCreateView -----
comment_list_get = swagger_auto_schema(
    operation_summary="댓글 목록 조회",
    operation_description="특정 게시글의 댓글을 모두 조회합니다.",
    responses={200: CommentSerializer(many=True)},
    tags=TAG,
)

comment_create_post = swagger_auto_schema(
    operation_summary="댓글 작성",
    operation_description="특정 게시글에 댓글을 작성합니다.",
    request_body=CommentSerializer,
    responses={201: CommentSerializer, 400: "유효성 검사 실패"},
    tags=TAG,
)


# ----- CommentDetailView -----
comment_update_put = swagger_auto_schema(
    operation_summary="댓글 수정 (전체)",
    operation_description="작성자만 댓글을 전체 수정할 수 있습니다.",
    request_body=CommentSerializer,
    responses={200: CommentSerializer, 403: "권한 없음", 400: "유효성 검사 실패"},
    tags=TAG,
)

comment_update_patch = swagger_auto_schema(
    operation_summary="댓글 수정 (일부)",
    operation_description="작성자만 댓글을 일부 수정할 수 있습니다.",
    request_body=CommentSerializer,
    responses={200: CommentSerializer, 403: "권한 없음", 400: "유효성 검사 실패"},
    tags=TAG,
)

comment_delete = swagger_auto_schema(
    operation_summary="댓글 삭제",
    operation_description="작성자만 댓글을 삭제할 수 있습니다.",
    responses={204: "댓글 삭제 완료", 403: "권한 없음"},
    tags=TAG,
)
