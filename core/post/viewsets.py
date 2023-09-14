from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from core.abstract.viewsets import AbstractViewSet
from core.auth.permissions import UserPermission
from .models import Post
from .serializers import PostSerializer

class PostViewSet(AbstractViewSet):
    http_method_names = ('post','get','put','delete')
    permission_classes = (UserPermission,)
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
    
    # 좋아요를 추가삭제할 게시물을 검색 - self.get_object() 메서드는 detail 속성이 True로 설정되어 있기 때문에 URL 요청에 전달된 ID를 사용하여 해당 게시물을 자동 반환
    # self.request 객체에서 요청을 한 사용자도 검색 - remove_like 또는 like 메서드를 호출할 수 있따.
    # self.serializer_class에 정의된 Serializer 클래스를 사용하여 게시물을 직렬화 하고 응답을 반환

    # api/post/post_pk/like/
    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.like(post)
        serializer = self.serializer_class(post)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # api/post/post_pk/remove_like/
    @action(methods=['post'], detail=True)
    def remove_like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.remove_like(post)
        serializer = self.serializer_class(post)

        return Response(serializer.data, status=status.HTTP_200_OK)