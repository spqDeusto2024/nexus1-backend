import pytest
from unittest.mock import patch, MagicMock
from app.controllers.parameter_room_handler import ParameterRoom_Controller
from app.models.models import ParameterRoomCreate, ParameterRoomDelete, ParameterRoomUpdate
from app.models.response_models import ResponseModel
from datetime import datetime


@pytest.fixture
def controller():
    """Fixture to initialize the controller."""
    return ParameterRoom_Controller()


@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.healthz', return_value={"status": "ok"})
def test_healthz(mock_healthz, controller):
    """Test for the healthz method."""
    response = controller.healthz()
    assert response == {"status": "ok"}


@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.create_parameterRoom')
def test_create_parameterroom(mock_create, controller):
    """Test for the create_parameterRoom method."""
    # Simula la respuesta de create_parameterRoom
    mock_response = ResponseModel(
        status="ok",
        message="ParameterRoom inserted into database successfully",
        data=None,
        code=201
    )
    mock_create.return_value = mock_response

    # Llama al método con datos de prueba
    body = ParameterRoomCreate(
        id_room=1,
        id_parameter=2,
        date=datetime.now(),
        value=42.5,
        created_at=datetime.now()
    )
    response = controller.create_parameterRoom(body)

    # Assertions para verificar que la respuesta es correcta
    assert response.status == "ok"
    assert response.message == "ParameterRoom inserted into database successfully"
    assert response.data is None
    assert response.code == 201


@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.get_all')
def test_get_all_parameterrooms(mock_get_all, controller):
    """Test for the get_all method."""
    # Mock the response of get_all
    mock_parameterrooms = [
        MagicMock(id_room=1, id_parameter=2, value=42.5),
        MagicMock(id_room=3, id_parameter=4, value=24.5),
    ]

    mock_response = ResponseModel(
        status="ok",
        message="All ParametersRooms successfully retrieved",
        data=mock_parameterrooms,
        code=201
    )
    mock_get_all.return_value = mock_response

    # Llama al método
    response = controller.get_all()

    # Assertions
    assert response.status == "ok"
    assert response.message == "All ParametersRooms successfully retrieved"
    assert len(response.data) == 2


@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.delete_parameterRoom')
def test_delete_parameterroom(mock_delete, controller):
    """Test for the delete_parameterRoom method."""
    # Mock the response of delete_parameterRoom
    mock_response = ResponseModel(
        status="ok",
        message="ParameterRoom successfully deleted",
        data=None,
        code=200
    )
    mock_delete.return_value = mock_response

    # Prepara el body para la solicitud de eliminación
    body = ParameterRoomDelete(id=1)

    # Llama al método
    response = controller.delete_parameterRoom(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "ParameterRoom successfully deleted"


@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.update_parameterRoom')
def test_update_parameterroom(mock_update, controller):
    """Test for the update_parameterRoom method."""
    # Mock the response of update_parameterRoom
    mock_response = ResponseModel(
        status="ok",
        message="ParameterRoom successfully updated",
        data=None,
        code=200
    )
    mock_update.return_value = mock_response

    # Prepara el body para la solicitud de actualización
    body = ParameterRoomUpdate(
        id=1,
        id_room=1,
        id_parameter=2,
        date=datetime.now(),
        value=50.0
    )

    # Llama al método
    response = controller.update_parameterRoom(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "ParameterRoom successfully updated"




#TEST PARA EXCEPCIONES:
@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.create_parameterRoom')
def test_create_parameterroom_database_error(mock_create, controller):
    """Test for create_parameterRoom handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Database connection failed",
        data=None,
        code=500
    )
    mock_create.return_value = mock_response

    # Prepara datos de prueba
    body = ParameterRoomCreate(
        id_room=1,
        id_parameter=2,
        date=datetime.now(),
        value=42.5,
        created_at=datetime.now()
    )

    # Llama al método
    response = controller.create_parameterRoom(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Database connection failed"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.get_all')
def test_get_all_parameterrooms_database_error(mock_get_all, controller):
    """Test for get_all handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to retrieve ParameterRooms from database",
        data=None,
        code=500
    )
    mock_get_all.return_value = mock_response

    # Llama al método
    response = controller.get_all()

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to retrieve ParameterRooms from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.delete_parameterRoom')
def test_delete_parameterroom_database_error(mock_delete, controller):
    """Test for delete_parameterRoom handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to delete ParameterRoom from database",
        data=None,
        code=500
    )
    mock_delete.return_value = mock_response

    # Prepara el body para la solicitud de eliminación
    body = ParameterRoomDelete(id=999)  # Un ID inexistente

    # Llama al método
    response = controller.delete_parameterRoom(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to delete ParameterRoom from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.parameter_room_handler.ParameterRoom_Controller.update_parameterRoom')
def test_update_parameterroom_database_error(mock_update, controller):
    """Test for update_parameterRoom handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to update ParameterRoom in database",
        data=None,
        code=500
    )
    mock_update.return_value = mock_response

    # Prepara datos de prueba
    body = ParameterRoomUpdate(
        id=999,  # Un ID inexistente
        id_room=1,
        id_parameter=2,
        date=datetime.now(),
        value=50.0
    )

    # Llama al método
    response = controller.update_parameterRoom(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to update ParameterRoom in database"
    assert response.data is None
    assert response.code == 500
