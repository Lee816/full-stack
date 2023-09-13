from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework import status

from core.abstract.viewsets import AbstractViewSet
from .models import Post
from .serializers import PostSerializer

# Django 구너한은 보통 두 단계에서 작동 - 전체엔드포인드(has_permisson) 와 객체 수준(has_object_permission)
# 권한을 작성하는 좋은 방법은 항상 기본적으로 거부하는것
# 익명 사용자는 SAFE_METHODS (GET, OPTIONS, HEAD) 요청만 할 수 있게 했다.
class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        
        if view.basename in ['post']:
            return bool(request.user and request.user.is_authenticated)

        return False
    
    def has_permission(self, request, view):
        if view.basename in ['post']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            
            return bool(request.user and request.user.is_authenticated)
        
        return False

class PostViewSet(AbstractViewSet):
    http_method_names = ('post','get')
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    
    # 모든 게시물을 반환한다. 
    # 특별한 요구사항이 없으므로 데이터베이스의 모든 게시물을 반환할 수 있다.
    def get_queryset(self):
        return Post.objects.all()
    
    # URL에 있을 public_id를 사용하여 게시물 객체를 반환한다.
    # 이 매개변수는 self.kwargs 디렉토리에서 검색
    def get_object(self):
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        
        return obj

    # ViewSet에 연결된 endpoint에서 POST 요청에 대해 실행되는 Viewset액션
    # 데이터를 Viewset에 선언된 serializer로 전달하고, 데이터를 검증한 다음 perform_create 메서드를 호출하여 게시물 객체를 생성
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)