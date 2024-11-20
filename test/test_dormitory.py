import pytest
from unittest.mock import patch, MagicMock
from app.controllers.dormitory_handler import Dormitory_Controller
from app.models.models import DormitoryCreate, DormitoryDelete, DormitoryUpdate
from app.models.response_models import ResponseModel
from datetime import datetime

@pytest.fixture
def controller():
    """Fixture to initialize the controller."""
    return Dormitory_Controller()


@patch('app.controllers.dormitory_handler.Dormitory_Controller.healthz', return_value={"status": "ok"})
def test_healthz(mock_healthz, controller):
    """Test for the healthz method."""
    response = controller.healthz()
    assert response == {"status": "ok"}


@patch('app.controllers.dormitory_handler.Dormitory_Controller.create_dormitory')
def test_create_dormitory(mock_create, controller):
    """Test for the create_dormitory method."""
    # Simula la respuesta de create_dormitory
    mock_response = ResponseModel(
        status="ok",
        message="Dormitory inserted into database successfully",
        data=None,
        code=201
    )
    mock_create.return_value = mock_response  # Aquí usamos el objeto real de ResponseModel.

    # Llama al método con datos de prueba
    body = DormitoryCreate(
        id_shelter=1,
        name="Dormitory A",
        description="First dormitory",
        capacity=100,
        actual_tenant_number=50,
        availability=True,
        created_at=datetime.now()
    )
    response = controller.create_dormitory(body)

    # Assertions para verificar que la respuesta es correcta
    assert response.status == "ok"
    assert response.message == "Dormitory inserted into database successfully"
    assert response.data is None
    assert response.code == 201


@patch('app.controllers.dormitory_handler.Dormitory_Controller.get_all')
def test_get_all(mock_get_all, controller):
    """Test for the get_all method."""
    # Mock the response of get_all

    mock_dormitories = [
        MagicMock(name="Dormitory A", id_shelter=1, capacity=100),
        MagicMock(name="Dormitory B", id_shelter=2, capacity=200),
    ]

    mock_response = ResponseModel(
        status="ok",
        message="All dormitories successfully retrieved",
        data=mock_dormitories,
        code=201
    )
    
    mock_get_all.return_value = mock_response
    response = controller.get_all()
    
    # Assertions
    assert response.status == "ok"
    assert response.message == "All dormitories successfully retrieved"
    assert len(response.data) == 2


@patch('app.controllers.dormitory_handler.Dormitory_Controller.delete_dormitory')
def test_delete_dormitory(mock_delete, controller):
    """Test for the delete_dormitory method."""
    
    # Mock the response of delete_dormitory
    mock_response = ResponseModel(
        status="ok",
        message="Dormitory successfully deleted",
        data=None,
        code=200
    )
    mock_delete.return_value = mock_response
    
    # Prepare the body for the delete request
    body = DormitoryDelete(id=1)
    
    # Call the method
    response = controller.delete_dormitory(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Dormitory successfully deleted"


@patch('app.controllers.dormitory_handler.Dormitory_Controller.update_dormitory')
def test_update_dormitory(mock_update, controller):
    """Test for the update_dormitory method."""
    
    # Mock the response of update_dormitory
    mock_response = ResponseModel(
        status="ok",
        message="Dormitory successfully updated",
        data=None,
        code=200
    )
    mock_update.return_value = mock_response
    
    # Prepare the body for the update request
    body = DormitoryUpdate(
        id=1,
        id_shelter = 1,
        name="Updated Dormitory",
        description="Updated description",
        capacity=150,
        actual_tenant_number=75,
        availability=False,
        created_at=datetime.now()
    )
    
    # Call the method
    response = controller.update_dormitory(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Dormitory successfully updated"





#Test para excepciones
@patch('app.controllers.dormitory_handler.Dormitory_Controller.create_dormitory')
def test_create_dormitory_database_error(mock_create, controller):
    """Test for create_dormitory handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Database connection failed",
        data=None,
        code=500
    )
    mock_create.return_value = mock_response

    # Prepara datos de prueba
    body = DormitoryCreate(
        id_shelter=1,
        name="Dormitory A",
        description="First dormitory",
        capacity=100,
        actual_tenant_number=50,
        availability=True,
        created_at=datetime.now()
    )

    # Llama al método
    response = controller.create_dormitory(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Database connection failed"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.dormitory_handler.Dormitory_Controller.get_all')
def test_get_all_database_error(mock_get_all, controller):
    """Test for get_all handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to retrieve dormitories from database",
        data=None,
        code=500
    )
    mock_get_all.return_value = mock_response

    # Llama al método
    response = controller.get_all()

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to retrieve dormitories from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.dormitory_handler.Dormitory_Controller.delete_dormitory')
def test_delete_dormitory_database_error(mock_delete, controller):
    """Test for delete_dormitory handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to delete dormitory from database",
        data=None,
        code=500
    )
    mock_delete.return_value = mock_response

    # Prepara el body para la solicitud de eliminación
    body = DormitoryDelete(id=999)  # Un ID inexistente

    # Llama al método
    response = controller.delete_dormitory(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to delete dormitory from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.dormitory_handler.Dormitory_Controller.update_dormitory')
def test_update_dormitory_database_error(mock_update, controller):
    """Test for update_dormitory handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to update dormitory in database",
        data=None,
        code=500
    )
    mock_update.return_value = mock_response

    # Prepara datos de prueba
    body = DormitoryUpdate(
        id=999,  # Un ID inexistente
        id_shelter=1,
        name="Updated Dormitory",
        description="Updated description",
        capacity=150,
        actual_tenant_number=75,
        availability=False,
        created_at=datetime.now()
    )

    # Llama al método
    response = controller.update_dormitory(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to update dormitory in database"
    assert response.data is None
    assert response.code == 500

