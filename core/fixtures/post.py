import pytest

from core.post.models import Post
from .user import user

@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user, body='Test Post Body')