from unittest.mock import Mock

from api.posts import PostsAPI
from conftest import posts_api


def test_get_post_delegates_request_to_client():
    # Arrange: create a fake client
    client = Mock()
    posts_api = PostsAPI(client)

    # Act: call the method we want to test
    posts_api.get_post(42)

    # Assert: verify how PostsAPI used its dependency
    client.get.assert_called_once_with('/posts/42')

def test_get_post_returns_client_response():
    client = Mock()
    expected_response = Mock()
    client.get.return_value = expected_response

    posts_api = PostsAPI(client)

    response = posts_api.get_post(42)

    assert response is expected_response


def test_create_post_sends_payload_as_json():
    client = Mock()
    posts_api = PostsAPI(client)

    payload = {
        "userId": 5,
        "title": "Test title",
        "body": "Test body",
    }

    posts_api.create_post(payload)

    client.post.assert_called_once_with(
        "/posts",
        json=payload,
    )