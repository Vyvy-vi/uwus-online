import pytest
from starlette.testclient import TestClient

from src.main import app


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as test_client:
        yield test_client
