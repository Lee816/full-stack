from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.user.serializers import UserSerializer
from core.post.models import Post
from .models import Comment

class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')

    class Meta:
        model = Comment
        fields = ['id','post','body','author','edited','created','updated']
        read_only_fields = ['edited']
        
    def validate_author(self, value):
        if self.context['request'].user != value:
            raise ValidationError("You can't create a comment for another user.")

        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data

        return rep
    
    # delete, put, patch 요청이 오면 수정될 객체를 가지고 있는 instance 속성을 제공
    # get, post 요청은 none 으로 설정
    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)

        return instance
    