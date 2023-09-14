import pytest

from core.user.models import User

data_user = {
    "username": "test_user",
    "email": "test@gamil.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "test_password"
}

# 데코레이터를 이용해 함수를 fixture로 지정한다.
# user 함수를 다른 테스트에서 임포트해 테스트 인자로 전달할 수 있다.
@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user)