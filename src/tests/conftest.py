from unittest.mock import Mock
from fastapi.testclient import TestClient
import requests
from src.auth.dependencies import AccessTokenBearer
from src import app
import pytest

mock_user_service = Mock()
mock_task_service = Mock()
mock_requests = Mock()

access_token_bearer = AccessTokenBearer()
app.dependency_overrides[access_token_bearer] = Mock()


app.dependency_overrides[requests] = Mock()

@pytest.fixture
def fake_user_service():
    return mock_user_service


@pytest.fixture
def fake_task_service():
    return mock_task_service

@pytest.fixture
def fake_access_token():
    return access_token_bearer


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def fake_requests():
    return mock_requests



