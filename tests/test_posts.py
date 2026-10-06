
import pytest

from conftest import posts_api
from factories.post_factory import create_post


@pytest.mark.parametrize(
    "post_id", [1,50,100]
)

def test_get_existing_post(posts_api, post_id):

    response = posts_api.get_post(post_id)

    assert response.status_code == 200

    assert response.json()["id"] == post_id

@pytest.mark.parametrize(
    "post_id",
    [0, 101, 999]
)
def test_get_non_existing_post(posts_api, post_id):

    response = posts_api.get_post(post_id)

    assert response.status_code == 404


def test_get_posts(posts_api):

    response = posts_api.get_posts()

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, list)
    assert len(body) == 100


def test_get_posts_have_expected_structure(posts_api):

    response = posts_api.get_posts()

    assert response.status_code == 200

    posts = response.json()

    for post in posts:
        assert "id" in post
        assert "userId" in post
        assert "title" in post
        assert "body" in post


def test_create_multiple_posts(posts_api):

    posts = [
        create_post(
            user_id=1,
            title="First post",
            body="First body"
        ),
        create_post(
            user_id=2,
            title="Second post",
            body="Second body"
        ),
        create_post(
            user_id=1,
            title="Third post",
            body="Third body"
        )
    ]
    for post in posts:

        response = posts_api.create_post(post.to_payload())

        assert response.status_code == 201

        body = response.json()

        assert body["title"] == post.title
        assert body["body"] == post.body
        assert body["userId"] == post.user_id
        assert "id" in body

@pytest.mark.parametrize(
    "user_id",
    [1, 2, 5]
)
def test_create_post_for_different_users(posts_api, user_id):
    post = create_post(user_id=user_id)

    response = posts_api.create_post(post.to_payload())

    assert response.status_code == 201

    body = response.json()

    assert body["userId"] == post.user_id

def test_create_post(posts_api, post):

    response = posts_api.create_post(
        post.to_payload()
    )

    assert response.status_code == 201

    body = response.json()

    assert body["userId"] == post.user_id
    assert body["title"] == post.title
    assert body["body"] == post.body
    assert "id" in body

@pytest.mark.parametrize(
    "user_id",
    [1,2,5]
)
def test_get_posts_by_user(posts_api, user_id):

    response = posts_api.get_posts(userId=user_id)

    assert response.status_code == 200

    posts = response.json()

    assert len(posts) > 0

    for post in posts:
        assert post["userId"] == user_id


def test_update_post(posts_api):

    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }

    response = posts_api.update_post(1, payload)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["title"] == "Updated title"
    assert body["body"] == "Updated body"
    assert body["userId"] == 1


def test_patch_post(posts_api):

    payload = {
        "title": "New title"
    }

    response = posts_api.patch_post(1, payload)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["title"] == "New title"


def test_delete_post(posts_api):

    response = posts_api.delete_post(1)

    assert response.status_code == 200


def test_get_post_comments(posts_api):

    response = posts_api.get_post_comments(1)

    assert response.status_code == 200

    comments = response.json()

    assert isinstance(comments, list)

    for comment in comments:
        assert comment["postId"] == 1


