from models.post import Post

def create_post(
        user_id=1,
        title="Test title",
        body="Test body"
):
    return Post(
        user_id = user_id,
        title = title,
        body = body
    )

