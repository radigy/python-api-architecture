import pytest

from api.posts import PostsAPI
from client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def posts_api(api_client):
    return PostsAPI(api_client)

