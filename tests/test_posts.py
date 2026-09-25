
def test_get_post(api_client):

    response = api_client.get(
        "/posts/1"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["userId"] == 1
    assert "title" in body
    assert "body" in body