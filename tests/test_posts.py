import pytest

from conftest import posts_api
from data.posts import NEW_POST


@pytest.mark.parametrize(
    "post_id", [1,50,100]
)

def test_get_existing_post(posts_api, post_id):

    response = posts_api.get_post(post_id)

    assert response.status_code == 200

    assert response.json()["id"] == post_id


def test_get_non_existing_post(posts_api):

    response = posts_api.get_post(999)

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


def test_create_post(posts_api):

    response = posts_api.create_post(NEW_POST)

    assert response.status_code == 201
