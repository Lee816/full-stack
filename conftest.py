import pytest

from rest_framework.test import APIClient

# 사용자 정의 클라이언트를 위한 fixture 함수
@pytest.fixture
def client():
    return APIClient()