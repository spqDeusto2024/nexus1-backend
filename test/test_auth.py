import pytest
from unittest.mock import patch, MagicMock
from app.controllers.auth_handler import Auth_Controller
from app.models.models import LoginCredentials
from app.models.response_models import ResponseModel
from app.auth.jwt_handler import create_access_token
from fastapi import HTTPException
from app.utils.hashing import hash_password
from app.auth.jwt_handler import create_access_token


@pytest.fixture
def controller():
    """Fixture to initialize the controller."""
    return Auth_Controller()


@patch('app.controllers.auth_handler.Administrator_Controller.get_admin_by_username')
@patch('app.auth.jwt_handler.create_access_token')
def test_login(mock_create_token, mock_get_admin_by_username, controller):
    """Test for the login method."""
    # Mock the response of get_admin_by_username
    mock_admin = MagicMock(username="testuser", password=hash_password("hashed_password"))
    mock_get_admin_by_username.return_value = ResponseModel(
        status="ok",
        message="Administrator retrieved successfully",
        data=mock_admin,
        code=200
    )

    # Mock the response of create_access_token
    mock_token = create_access_token({"sub": "testuser"})
    mock_create_token.return_value = mock_token
    
    # Prepare the credentials data for the request
    credentials = LoginCredentials(username="testuser", password="hashed_password")

    # Call the method
    response = controller.login(credentials)

    # Assertions:We look that token structure is ok
    assert response["access_token"].count(".") == 2  # Verifica que tenga las 3 partes (header, payload, signature)
    assert response["access_token"].startswith("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.")  # Verifica que comience como un JWT
    


@patch('app.controllers.auth_handler.Administrator_Controller.get_admin_by_username')
def test_login_invalid_username(mock_get_admin_by_username, controller):
    """Test for the login method with an invalid username."""
    # Mock the response of get_admin_by_username
    mock_get_admin_by_username.return_value = ResponseModel(
        status="error",
        message="Administrator not found",
        data=None,
        code=404
    )

    # Prepare the credentials data for the request
    credentials = LoginCredentials(username="invaliduser", password=hash_password("hashed_password"))

    # Call the method and check for HTTPException
    with pytest.raises(HTTPException) as exc_info:
        controller.login(credentials)
    
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid username or password"


@patch('app.controllers.auth_handler.Administrator_Controller.get_admin_by_username')
def test_login_invalid_password(mock_get_admin_by_username, controller):
    """Test for the login method with an invalid password."""
    # Mock the response of get_admin_by_username
    mock_admin = MagicMock(username="testuser", password=hash_password("hashed_password"))
    mock_get_admin_by_username.return_value = ResponseModel(
        status="ok",
        message="Administrator retrieved successfully",
        data=mock_admin,
        code=200
    )

    # Prepare the credentials data for the request with an incorrect password
    credentials = LoginCredentials(username="testuser", password=hash_password("hashed_password"))

    # Call the method and check for HTTPException
    with pytest.raises(HTTPException) as exc_info:
        controller.login(credentials)
    
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid username or password"
