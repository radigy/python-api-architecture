class UsersAPI:

    def __init__(self, client):
        self.client = client

    def get_user(self, user_id):
        return self.client.get(f"/users/{user_id}")

    def get_users(self):
        return self.client.get("/users")
