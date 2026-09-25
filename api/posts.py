
class PostsAPI:

    def __init__(self, client):
        self.client = client

    def get_post(self, post_id):
        return self.client.get(f"/posts/{post_id}")

    def get_posts(self):
        return self.client.get("/posts")

    def create_post(self, payload):
        return self.client.post("/posts", json=payload)

    def update_post(self, post_id, payload):
        return self.client.put(f"/posts/{post_id}", json=payload)

