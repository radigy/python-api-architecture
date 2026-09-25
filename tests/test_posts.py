
def test_get_post(posts_api):

    response = posts_api.get_post(1)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["userId"] == 1
    assert "title" in body
    assert "body" in body