from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from core.abstract.viewsets import AbstractViewSet
from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserViewSet(AbstractViewSet):
    http_method_names = ('patch','get')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    # 뷰셋이 모든 사용자의 목록을 얻기 위해 사용, 이 메서드는 /user/에 get 요청이 들어올때 호출
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        
        return User.objects.exclude(is_superuser=True)

    # 뷰셋이 한명의 사용자를 얻기 위해 사용, 이 메서드는 /user/id/ 엔드포인트에 get 또는 put 요청이 있을때 호출되며, pk는 사용자의 ID를 나타낸다.
    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)

        return obj
    
