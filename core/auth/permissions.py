from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

# Django 구너한은 보통 두 단계에서 작동 - 전체엔드포인드(has_permisson) 와 객체 수준(has_object_permission)
# 권한을 작성하는 좋은 방법은 항상 기본적으로 거부하는것
# 익명 사용자는 SAFE_METHODS (GET, OPTIONS, HEAD) 요청만 할 수 있게 했다.
class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        
        if view.basename in ['post','post-comment']:
            return bool(request.user and request.user.is_authenticated)

        return False
    
    def has_permission(self, request, view):
        if view.basename in ['post','post-comment']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            
            return bool(request.user and request.user.is_authenticated)
        
        return False