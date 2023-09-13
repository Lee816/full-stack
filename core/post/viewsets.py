from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.abstract.viewsets import AbstractViewSet
from .models import Post
from .serializers import PostSerializer

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