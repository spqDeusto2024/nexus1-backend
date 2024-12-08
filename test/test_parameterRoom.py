import pytest
from sqlalchemy.orm import Session
from datetime import datetime
from app.controllers.parameter_room_handler import ParameterRoom_Controller
from app.controllers.room_handler import Room_Controller
from app.controllers.parameter_handler import Parameter_Controller
from app.controllers.shelter_handler import Shelter_Controller
import app.models.models as models
import app.mysql.models as mysql_models
from mysql import TestDataBase  # Clase para manejar la base de datos
from app.models.response_models import ResponseModel

@pytest.fixture(scope="module")
def db_session():
    """
    Fija una sesión de base de datos para pruebas.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta tu configuración
    session = db.get_session()
    yield session
    session.close()

def test_healthz():
    """
    Prueba el endpoint de salud.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)
    result = controller.healthz()
    assert result == {"status": "ok"}

def test_create_parameterRoom(db_session):
    """
    Prueba la creación de un nuevo `ParameterRoom`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)
    room_controller = Room_Controller(db)
    parameter_controller = Parameter_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un parámetro
    parameter_data = models.ParameterCreate(
        name="parameter_testing",
        description="parameter for parameter_room testing",
        max_value=100.0,
        min_value=0.0,
        created_at=datetime.now()
    )
    response_parameter = parameter_controller.create_parameter(parameter_data)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Test Shelter",
        description="Shelter for room testing",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un room asociado al shelter
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="test_room",
        capacity=5,
        created_at=datetime.now()
    )
    response_room = room_controller.create_room(room_data)

    # Crear un `ParameterRoom`
    parameterRoom_data = models.ParameterRoomCreate(
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=6.9,
        created_at=datetime.now()
    )
    response = controller.create_parameterRoom(parameterRoom_data)

    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "ParameterRoom inserted into database successfully"
    assert response.data.value == 6.9

def test_get_all_parameterRooms(db_session):
    """
    Prueba la obtención de todos los `ParameterRooms`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)

    # Obtener todos los `ParameterRooms`
    response = controller.get_all()

    assert response.status == "ok"
    assert response.code == 200
    assert isinstance(response.data, list)
    assert len(response.data) > 0  # Se espera al menos un registro

def test_update_parameterRoom(db_session):
    """
    Prueba la actualización de un `ParameterRoom`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)
    room_controller = Room_Controller(db)
    parameter_controller = Parameter_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un parámetro
    parameter_data = models.ParameterCreate(
        name="parameter_to_update",
        description="parameter for updating",
        max_value=50.0,
        min_value=10.0,
        created_at=datetime.now()
    )
    response_parameter = parameter_controller.create_parameter(parameter_data)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Update Shelter",
        description="Shelter for updating room",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un room asociado al shelter
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="update_room",
        capacity=3,
        created_at=datetime.now()
    )
    response_room = room_controller.create_room(room_data)

    # Crear un `ParameterRoom`
    parameterRoom_data = models.ParameterRoomCreate(
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=8.3,
        created_at=datetime.now()
    )
    response_create = controller.create_parameterRoom(parameterRoom_data)

    # Actualizar el `ParameterRoom`
    updated_data = models.ParameterRoomUpdate(
        id=response_create.data.id,
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=20.5
    )
    response = controller.update_parameterRoom(updated_data)

    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "ParameterRoom successfully updated"

def test_delete_parameterRoom(db_session):
    """
    Prueba la eliminación de un `ParameterRoom`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)
    room_controller = Room_Controller(db)
    parameter_controller = Parameter_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un parámetro
    parameter_data = models.ParameterCreate(
        name="parameter_to_delete",
        description="parameter for deletion",
        max_value=100.0,
        min_value=0.0,
        created_at=datetime.now()
    )
    response_parameter = parameter_controller.create_parameter(parameter_data)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Delete Shelter",
        description="Shelter for deletion",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un room asociado al shelter
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="delete_room",
        capacity=10,
        created_at=datetime.now()
    )
    response_room = room_controller.create_room(room_data)

    # Crear un `ParameterRoom`
    parameterRoom_data = models.ParameterRoomCreate(
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=99.9,
        created_at=datetime.now()
    )
    response_create = controller.create_parameterRoom(parameterRoom_data)

    # Eliminar el `ParameterRoom`
    delete_data = models.ParameterRoomDelete(id=response_create.data.id)
    response = controller.delete_parameterRoom(delete_data)

    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "ParameterRoom successfully deleted"
