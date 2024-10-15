from unittest.mock import patch, MagicMock
import pytest

auth_prefix = f"/api/v1/auth"


@pytest.fixture
def mock_requests_post():
    # Create a MagicMock object to mock requests.get
    with patch('requests.post') as mock_get:
        # Prepare a mock response object with necessary methods
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "session": {
              "accessToken": "SECRETE_ACCESS_TOKEN",
              "refreshToken": "SECRETE_REFRESH_TOKEN",
              "accessTokenExpiresIn": 900,
              "user": {
                "email": "john.doe@gmail.com"
              }
            }
        }
        mock_response.status_code = 200
        # mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response
        yield mock_get


def test_user_creation(fake_user_service, test_client, mock_requests_post):
    signup_data = {
      "email": "john.doe@gmail.com",
      "first_name": "John",
      "last_name": "Doe",
      "password": "123456789"
    }

    response = test_client.post(
        url=f"{auth_prefix}/signup/email-password",
        json=signup_data,
    )

    assert response.status_code == 200


