import pytest
from unittest.mock import patch, MagicMock
from app.controllers.role_handler import Role_Controller
from app.models.models import RoleCreate, RoleDelete, RoleUpdate
from app.models.response_models import ResponseModel
from datetime import datetime

@pytest.fixture
def controller():
    """Fixture to initialize the controller."""
    return Role_Controller()


@patch('app.controllers.role_handler.Role_Controller.healthz', return_value={"status": "ok"})
def test_healthz(mock_healthz, controller):
    """Test for the healthz method."""
    response = controller.healthz()
    assert response == {"status": "ok"}


@patch('app.controllers.role_handler.Role_Controller.create_role')
def test_create_role(mock_create, controller):
    """Test for the create_role method."""
    # Simula la respuesta de create_role
    mock_response = ResponseModel(
        status="ok",
        message="Role inserted into database successfully",
        data=None,
        code=201
    )
    mock_create.return_value = mock_response

    # Llama al método con datos de prueba
    body = RoleCreate(name="TestRole", description="Test Description", id_room_relationship=1, created_at=datetime.now())
    response = controller.create_role(body)

    # Assertions para verificar que la respuesta es correcta
    assert response.status == "ok"
    assert response.message == "Role inserted into database successfully"
    assert response.data is None
    assert response.code == 201


@patch('app.controllers.role_handler.Role_Controller.get_all')
def test_get_all_roles(mock_get_all, controller):
    """Test for the get_all method."""
    # Mock the response of get_all

    mock_roles = [
        MagicMock(name="Role1", description="Description1"),
        MagicMock(name="Role2", description="Description2"),
    ]

    mock_response = ResponseModel(
        status="ok",
        message="All Roles successfully retrieved",
        data=mock_roles,
        code=201
    )
    mock_get_all.return_value = mock_response

    # Llama al método
    response = controller.get_all()

    # Assertions
    assert response.status == "ok"
    assert response.message == "All Roles successfully retrieved"
    assert len(response.data) == 2


@patch('app.controllers.role_handler.Role_Controller.delete_role')
def test_delete_role(mock_delete, controller):
    """Test for the delete_role method."""
    # Mock the response of delete_role
    mock_response = ResponseModel(
        status="ok",
        message="Role successfully deleted",
        data=None,
        code=200
    )
    mock_delete.return_value = mock_response

    # Prepara el body para la solicitud de eliminación
    body = RoleDelete(id=1)

    # Llama al método
    response = controller.delete_role(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Role successfully deleted"


@patch('app.controllers.role_handler.Role_Controller.update_role')
def test_update_role(mock_update, controller):
    """Test for the update_role method."""
    # Mock the response of update_role
    mock_response = ResponseModel(
        status="ok",
        message="Role successfully updated",
        data=None,
        code=200
    )
    mock_update.return_value = mock_response

    # Prepara el body para la solicitud de actualización
    body = RoleUpdate(id=1, name="UpdatedRole", description="Updated Description", id_room_relationship=2)

    # Llama al método
    response = controller.update_role(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Role successfully updated"


@patch('app.controllers.role_handler.Role_Controller.get_all')
def test_get_role_by_name(mock_get_all, controller):
    """Test for retrieving roles by their name."""
    # Mock the response
    mock_response = ResponseModel(
        status="ok",
        message="Role retrieved successfully",
        data={"name": "TestRole", "description": "Test Description"},
        code=200
    )
    mock_get_all.return_value = mock_response

    # Llama al método
    response = controller.get_all()

    # Assertions
    assert response.status == "ok"
    assert response.message == "Role retrieved successfully"
    assert response.data.get("name") == "TestRole"




#EXCEPTIONS TESTS
@patch('app.controllers.role_handler.Role_Controller.create_role')
def test_create_role_database_error(mock_create, controller):
    """Test for create_role handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Database connection failed",
        data=None,
        code=500
    )
    mock_create.return_value = mock_response

    # Prepara datos de prueba
    body = RoleCreate(name="TestRole", description="Test Description", id_room_relationship=1, created_at=datetime.now())

    # Llama al método
    response = controller.create_role(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Database connection failed"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.role_handler.Role_Controller.get_all')
def test_get_all_roles_database_error(mock_get_all, controller):
    """Test for get_all handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to retrieve roles from database",
        data=None,
        code=500
    )
    mock_get_all.return_value = mock_response

    # Llama al método
    response = controller.get_all()

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to retrieve roles from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.role_handler.Role_Controller.delete_role')
def test_delete_role_database_error(mock_delete, controller):
    """Test for delete_role handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to delete role from database",
        data=None,
        code=500
    )
    mock_delete.return_value = mock_response

    # Prepara datos de prueba
    body = RoleDelete(id=999)  # Un ID inexistente

    # Llama al método
    response = controller.delete_role(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to delete role from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.role_handler.Role_Controller.update_role')
def test_update_role_database_error(mock_update, controller):
    """Test for update_role handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to update role in database",
        data=None,
        code=500
    )
    mock_update.return_value = mock_response

    # Prepara datos de prueba
    body = RoleUpdate(id=999, name="UpdatedRole", description="Updated Description", id_room_relationship=2)

    # Llama al método
    response = controller.update_role(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to update role in database"
    assert response.data is None
    assert response.code == 500


