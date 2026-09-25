import requests

from config import BASE_URL


class APIClient:

    def get(self, endpoint, **kwargs):
        return requests.get(f"{BASE_URL}{endpoint}",
                            **kwargs
                            )

    def post(self, endpoint, **kwargs):
        return requests.post(
            f"{BASE_URL}{endpoint}",
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        return requests.put(
            f"{BASE_URL}{endpoint}",
            **kwargs
        )

    def patch(self, endpoint, **kwargs):
        return requests.patch(
            f"{BASE_URL}{endpoint}",
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        return requests.delete(
            f"{BASE_URL}{endpoint}",
            **kwargs
        )
