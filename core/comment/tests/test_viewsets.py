from rest_framework import status

from core.fixtures.user import user
from core.fixtures.post import post
from core.fixtures.comment import comment

class TestCommentViewSet:
    # 댓글 리소스는 게시물 리소스 하위에 중첩되어 있음
    endpoint = '/api/post/'

    def test_list(self, client, user, post, comment):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(post.public_id) + '/comment/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        
    def test_retrieve(self, client, user, post, comment):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(post.public_id) + '/comment/' + str(comment.public_id) + '/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == comment.public_id.hex
        assert response.data['body'] == comment.body
        assert response.data['author']['id'] == comment.author.public_id.hex
    
    