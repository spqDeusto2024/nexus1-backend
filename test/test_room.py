import pytest
from unittest.mock import patch, MagicMock
from app.controllers.room_handler import Room_Controller
from app.models.models import RoomCreate, RoomDelete, RoomUpdate
from app.models.response_models import ResponseModel
from datetime import datetime

@pytest.fixture
def controller():
    """Fixture to initialize the controller."""
    return Room_Controller()


@patch('app.controllers.room_handler.Room_Controller.healthz', return_value={"status": "ok"})
def test_healthz(mock_healthz, controller):
    """Test for the healthz method."""
    response = controller.healthz()
    assert response == {"status": "ok"}


@patch('app.controllers.room_handler.Room_Controller.create_room')
def test_create_room(mock_create, controller):
    """Test for the create_room method."""
    # Simula la respuesta de create_room
    mock_response = ResponseModel(
        status="ok",
        message="Room inserted into database successfully",
        data=None,
        code=201
    )
    mock_create.return_value = mock_response  # Aquí usamos el objeto real de ResponseModel.

    # Llama al método con datos de prueba
    body = RoomCreate(
        id_shelter=1,
        name="Room A",
        description="First room",
        capacity=100,
        actual_tenant_number=50,
        availability=True,
        created_at=datetime.now()
    )
    response = controller.create_room(body)

    # Assertions para verificar que la respuesta es correcta
    assert response.status == "ok"
    assert response.message == "Room inserted into database successfully"
    assert response.data is None
    assert response.code == 201


@patch('app.controllers.room_handler.Room_Controller.get_all')
def test_get_all(mock_get_all, controller):
    """Test for the get_all method."""
    # Mock the response of get_all

    mock_rooms = [
        MagicMock(name="Room, A", id_shelter=1, capacity=100),
        MagicMock(name="Room B", id_shelter=2, capacity=200),
    ]

    mock_response = ResponseModel(
        status="ok",
        message="All rooms successfully retrieved",
        data=mock_rooms,
        code=201
    )
    
    mock_get_all.return_value = mock_response
    response = controller.get_all()
    
    # Assertions
    assert response.status == "ok"
    assert response.message == "All rooms successfully retrieved"
    assert len(response.data) == 2


@patch('app.controllers.rooms_handler.Room_Controller.delete_room')
def test_delete_room(mock_delete, controller):
    """Test for the delete_room method."""
    
    # Mock the response of delete_room
    mock_response = ResponseModel(
        status="ok",
        message="Room successfully deleted",
        data=None,
        code=200
    )
    mock_delete.return_value = mock_response
    
    # Prepare the body for the delete request
    body = RoomDelete(id=1)
    
    # Call the method
    response = controller.delete_room(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Room successfully deleted"


@patch('app.controllers.room_handler.Room_Controller.update_room')
def test_update_room(mock_update, controller):
    """Test for the update_room method."""
    
    # Mock the response of update_room
    mock_response = ResponseModel(
        status="ok",
        message="Room successfully updated",
        data=None,
        code=200
    )
    mock_update.return_value = mock_response
    
    # Prepare the body for the update request
    body = RoomUpdate(
        id=1,
        id_shelter = 1,
        name="Updated Room",
        description="Updated description",
        capacity=150,
        actual_tenant_number=75,
        availability=False,
        created_at=datetime.now()
    )
    
    # Call the method
    response = controller.update_room(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Room successfully updated"





#Test para excepciones
@patch('app.controllers.room_handler.Room_Controller.create_room')
def test_create_room_database_error(mock_create, controller):
    """Test for create_room handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Database connection failed",
        data=None,
        code=500
    )
    mock_create.return_value = mock_response

    # Prepara datos de prueba
    body = RoomCreate(
        id_shelter=1,
        name="Room A",
        description="First room",
        capacity=100,
        actual_tenant_number=50,
        availability=True,
        created_at=datetime.now()
    )

    # Llama al método
    response = controller.create_room(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Database connection failed"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.room_handler.Room_Controller.get_all')
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

@patch('app.controllers.room_handler.Room_Controller.delete_room')
def test_delete_room_database_error(mock_delete, controller):
    """Test for delete_room handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to delete room from database",
        data=None,
        code=500
    )
    mock_delete.return_value = mock_response

    # Prepara el body para la solicitud de eliminación
    body = RoomDelete(id=-1)  # Un ID inexistente

    # Llama al método
    response = controller.delete_room(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to delete room from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.room_handler.Room_Controller.update_room')
def test_update_room_database_error(mock_update, controller):
    """Test for update_room handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to update room in database",
        data=None,
        code=500
    )
    mock_update.return_value = mock_response

    # Prepara datos de prueba
    body = RoomUpdate(
        id=-1,  # Un ID inexistente
        id_shelter=1,
        name="Updated Room",
        description="Updated description",
        capacity=150,
        actual_tenant_number=75,
        availability=False,
        created_at=datetime.now()
    )

    # Llama al método
    response = controller.update_room(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to update Room in database"
    assert response.data is None
    assert response.code == 500

