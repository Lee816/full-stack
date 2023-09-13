from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.user.serializers import UserSerializer
from .models import Post

class PostSerializer(AbstractSerializer):
    # SlugRelatedField()필드는 관계의 대상을 대상의 필드를사용하여 표현하는데 사용된다.
    # 게시물을 생성할 때 요청의 본문에 작성자의 public_id가 전달되어 사용자를 식별하고 게시물에 연결할 수 있다.
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')

    class Meta:
        model = Post
        fields = ['id','author','body','edited','created','updated']
        read_only_fields = ['edited']
    
    # author 필드에 대한 유효성 검사를 수행한다. - 게시물을 작성하는 사용자가 author 필드의 사용자와 동일한지 확인
    def validate_author(self, value):
        # 모든 serializer에는 context라는 딕려너리가 있다. 이 딕셔너리는 보통 요청 객체를 포함하고 있어 몇가지 확인을 수행하는데 사용할 수 있다.
        if self.context['request'].user != value:
            raise ValidationError("You can't create a post for another user.")

        return value
    
    # 직렬화가 필요한 객체 인스턴스를 받아들이고 원시 표현을 반환
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data

        return rep