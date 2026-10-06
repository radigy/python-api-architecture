from venv import create

import pytest

from api.posts import PostsAPI
from client import APIClient
from factories.post_factory import create_post

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def posts_api(api_client):
    return PostsAPI(api_client)

@pytest.fixture
def post():
    post =  create_post()
    yield post