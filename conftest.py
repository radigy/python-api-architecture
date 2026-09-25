import pytest

from client import APIClient

@pytest.fixture()
def api_client():
    return APIClient()

