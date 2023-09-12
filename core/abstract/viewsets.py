from rest_framework import viewsets, filters

class AbstractViewSet(viewsets.ModelViewSet):
    # 기본 필터 백엔드를 설정
    filter_backends = [filters.OrderingFilter]
    # 이 목록에는 요청을 할때 주문 매개변수로 사용할 수 있는 필드가 포함
    ordering_fields = ['updated','created']
    # 많은 객체를 응답으로 보낼 순서를 Django REST에 알려준다.
    ordering = ['-updated']