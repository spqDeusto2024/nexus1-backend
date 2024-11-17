import pytest
from unittest.mock import patch, MagicMock
from app.controllers.administrator_handler import Administrator_Controller
from app.models.models import AdministratorCreate, AdministratorDelete, AdministratorUpdate
from app.models.response_models import ResponseModel
from datetime import datetime

@pytest.fixture
def controller():
    """Fixture to initialize the controller."""
    return Administrator_Controller()


@patch('app.controllers.administrator_handler.Administrator_Controller.healthz', return_value={"status": "ok"})
def test_healthz(mock_healthz, controller):
    """Test for the healthz method."""
    response = controller.healthz()
    assert response == {"status": "ok"}


@patch('app.controllers.administrator_handler.Administrator_Controller.create_administrator')
def test_create_administrator(mock_create, controller):
    """Test for the create_administrator method."""
    # Simula la respuesta de create_administrator
    mock_response = ResponseModel(
        status="ok",
        message="Administrator inserted into database successfully",
        data=None,
        code=201
    )
    mock_create.return_value = mock_response  # Aquí usamos el objeto real de ResponseModel.

    # Llama al método con datos de prueba
    body = AdministratorCreate(username="testadmin", password="password123", created_at=datetime.now())
    response = controller.create_administrator(body)

    # Assertions para verificar que la respuesta es correcta
    assert response.status == "ok"
    assert response.message == "Administrator inserted into database successfully"
    assert response.data is None
    assert response.code == 201


@patch('app.controllers.administrator_handler.Administrator_Controller.get_all')
def test_get_all(mock_get_all, controller):
    """Test for the get_all method."""
    # Mock the response of get_all

    mock_administrators = [
        MagicMock(username="admin1", password="hashed_pass1"),
        MagicMock(username="admin2", password="hashed_pass2"),
    ]

    mock_response = ResponseModel(
                status="ok",
                message="All administrators successfully retrieved",
                data = mock_administrators,
                code=201
    )
    
    mock_get_all.return_value = mock_response
    response = controller.get_all()
    # Assertions
    assert response.status == "ok"
    assert response.message == "All administrators successfully retrieved"
    assert len(response.data) == 2


@patch('app.controllers.administrator_handler.Administrator_Controller.delete_administrator')
def test_delete_administrator(mock_delete, controller):
    """Test for the delete_administrator method."""
    
    # Mock the response of delete_administrator
    mock_response = ResponseModel(
        status="ok",
        message="Administrator successfully deleted",
        data=None,
        code=200
    )
    mock_delete.return_value = mock_response
    
    # Prepare the body for the delete request
    body = AdministratorDelete(id=1)
    
    # Call the method
    response = controller.delete_administrator(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Administrator successfully deleted"



@patch('app.controllers.administrator_handler.Administrator_Controller.update_administrator')
def test_update_administrator(mock_update, controller):
    """Test for the update_administrator method."""
    
    # Mock the response of update_administrator
    mock_response = ResponseModel(
        status="ok",
        message="Administrator successfully updated",
        data=None,
        code=200
    )
    mock_update.return_value = mock_response
    
    # Prepare the body for the update request
    body = AdministratorUpdate(id=1, username="updatedadmin", password="updatedpassword")
    
    # Call the method
    response = controller.update_administrator(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Administrator successfully updated"


@patch('app.controllers.administrator_handler.Administrator_Controller.get_admin_by_username')
def test_get_admin_by_username(mock_get_admin, controller):
    """Test for the get_admin_by_username method."""
    
    # Mock the response of get_admin_by_username
    mock_response = ResponseModel(
        status="ok",
        message="Administrator retrieved successfully",
        data={"username": "manuel"},
        code=200
    )
    mock_get_admin.return_value = mock_response
    
    # Prepare the username for the request
    username = "manuel"
    
    # Call the method
    response = controller.get_admin_by_username(username)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Administrator retrieved successfully"
    assert response.data.get("username") == username