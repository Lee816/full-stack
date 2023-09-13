from rest_framework import routers

from .user.viewsets import UserViewSet
from .auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from .post.viewsets import PostViewSet

router = routers.SimpleRouter()

# 뷰셋에 대한 라우트를 등록하기 위해서는 register() 메서드가 두 가지 인자가 필요하다.
# 접두사 - 기본적으로 엔드포인트의 이름
# 뷰셋 - 유효한 뷰셋 클래스만을 나타낸다.
# basename - 선택적 인자이지만 가독성을 높여주기 때문에 사용하는 것을 권장
router.register(r'user',UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'post', PostViewSet, basename='post')
urlpatterns = [
    *router.urls,
]