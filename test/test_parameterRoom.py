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

    #CREO EL PARAMETRO
    parameter_data = models.ParameterCreate(name="paremtert_testing", description="paramter_paraemter_room_testing",created_at = datetime.now())
    response_parameter = parameter_controller.create_parameter(parameter_data)

    #CREO EL SHLETER PARA EL ROOM
    shelter_data = models.ShelterCreate(name="New Shedescriptionlter", description="proving shelter",created_at = datetime.now())
    response_shelter = shelter_controller.create_shelter(shelter_data)

    #CREO EL ROOM
    room_data = models.RoomCreate(id_shelter = response_shelter.data.id ,name = "test_shelter",created_at = datetime.now())
    response_room = room_controller.create_room(room_data)



    parameterRoom_data = models.ParameterRoomCreate(
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=6.9,
        created_at = datetime.now()
    )
    response = controller.create_parameterRoom(parameterRoom_data)

    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "ParameterRoom inserted into database successfully"


def test_get_all_parameterRooms(db_session):
    """
    Prueba la obtención de todos los `ParameterRooms`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)
    response = controller.get_all()
    assert response.status == "ok"
    assert response.code == 200
    assert isinstance(response.data, list)
    assert len(response.data) > 0  # Se espera que haya al menos un registro


def test_update_parameterRoom(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)
    room_controller = Room_Controller(db)
    parameter_controller = Parameter_Controller(db)
    shelter_controller = Shelter_Controller(db)

    #CREO EL PARAMETRO
    parameter_data = models.ParameterCreate(name="Test_parameter_update", description="A parameter for testing_update",created_at = datetime.now())
    response_parameter = parameter_controller.create_parameter(parameter_data)

    #CREO EL SHLETER PARA EL ROOM
    shelter_data = models.ShelterCreate(name="New shelter update_3", description="A new shelter update_3",created_at = datetime.now())
    response_shelter = shelter_controller.create_shelter(shelter_data)

    #CREO EL ROOM
    room_data = models.RoomCreate(id_shelter = response_shelter.data.id ,name = "test_room update",created_at = datetime.now())
    response_room = room_controller.create_room(room_data)



    parameterRoom_data = models.ParameterRoomCreate(
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=8.3,
        created_at = datetime.now()
    )
    response = controller.create_parameterRoom(parameterRoom_data)

    # Actualiza el `ParameterRoom`
    updated_data = models.ParameterRoomUpdate(
        id=response.data.id,
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=53.2
    )
    response = controller.update_parameterRoom(updated_data)

    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "ParameterRoom successfully updated"
    # assert response.data.value == 53.2


def test_delete_parameterRoom(db_session):
    """
    Prueba la eliminación de un `ParameterRoom`.
    """
    # Crea un `ParameterRoom` inicial para eliminar
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = ParameterRoom_Controller(db)
    room_controller = Room_Controller(db)
    parameter_controller = Parameter_Controller(db)
    shelter_controller = Shelter_Controller(db)

    #CREO EL PARAMETRO
    parameter_data = models.ParameterCreate(name="Test Parameter_delete", description="A parameter for testing_delete",created_at = datetime.now())
    response_parameter = parameter_controller.create_parameter(parameter_data)

    #CREO EL SHLETER PARA EL ROOM
    shelter_data = models.ShelterCreate(name="New Shedescriptionlter_delete", description="A new shelter_delete",created_at = datetime.now())
    response_shelter = shelter_controller.create_shelter(shelter_data)

    #CREO EL ROOM
    room_data = models.RoomCreate(id_shelter = response_shelter.data.id ,name = "test_shelter_delete",created_at = datetime.now())
    response_room = room_controller.create_room(room_data)



    parameterRoom_data = models.ParameterRoomCreate(
        id_room=response_room.data.id,
        id_parameter=response_parameter.data.id,
        date=datetime.now(),
        value=63.0,
        created_at = datetime.now()
    )
    response = controller.create_parameterRoom(parameterRoom_data)

    # Elimina el `ParameterRoom`
    delete_data = models.ParameterRoomDelete(id=response.data.id)
    response = controller.delete_parameterRoom(delete_data)

    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "ParameterRoom successfully deleted"
