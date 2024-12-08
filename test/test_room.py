import pytest
from sqlalchemy.orm import Session
from app.models.models import *  # Importa los modelos Pydantic
from app.controllers.role_handler import Role_Controller  # Importa el controlador de roles
from mysql import TestDataBase  # Clase para la base de datos de pruebas
from sqlalchemy import create_engine
import app.mysql.models as mysql_models  # Modelo SQLAlchemy de Role
from datetime import datetime
from app.controllers.parameter_room_handler import ParameterRoom_Controller
from app.controllers.room_handler import Room_Controller
from app.controllers.parameter_handler import Parameter_Controller
from app.controllers.shelter_handler import Shelter_Controller
import app.models.models as models

@pytest.fixture(scope="module")
def db_session():
    # Crear una sesión de base de datos para usar en las pruebas
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta según tu configuración
    session = db.get_session()
    yield session
    session.close()

def test_create_room(db_session):
    """
    Prueba la creación de un nuevo `Room`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    room_controller = Room_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un shelter para asociarlo con el room
    shelter_data = models.ShelterCreate(
        name="Test Shelter de Carlos Gonzalez",
        description="Shelter for room testing for Carlos",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear el room
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="Test Room",
        description="Room for testing",
        capacity=5,
        actual_tenant_number=0,
        availability=True,
        created_at=datetime.now()
    )
    response_create = room_controller.create_room(room_data)

    # Validar que el room fue creado
    assert response_create.status == "ok"
    room_id = response_create.data.id
    assert room_id is not None
    assert response_create.code == 201
    assert response_create.message == "Room inserted into database successfully"

def test_get_all_rooms(db_session):
    """
    Prueba la obtención de todas las habitaciones.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    room_controller = Room_Controller(db)

    # Obtener todas las habitaciones
    response = room_controller.get_all()

    # Validaciones
    assert response.status == "ok"
    assert isinstance(response.data, list)
    assert response.code == 200

def test_delete_room(db_session):
    """
    Prueba la eliminación de un `Room`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    room_controller = Room_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un shelter para asociarlo con el room
    shelter_data = models.ShelterCreate(
        name="Shelter for Room Deletion",
        description="Test shelter for deletion",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear el room
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="Room to Delete",
        description="Room that will be deleted",
        capacity=3,
        actual_tenant_number=0,
        availability=True,
        created_at=datetime.now()
    )
    response_create = room_controller.create_room(room_data)
    room_id = response_create.data.id

    # Eliminar el room
    delete_data = models.RoomDelete(id=room_id)
    response = room_controller.delete_room(delete_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "Room successfully deleted"

def test_update_room(db_session):
    """
    Prueba la actualización de un `Room`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    room_controller = Room_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un shelter para asociarlo con el room
    shelter_data = models.ShelterCreate(
        name="Shelter for Room Update",
        description="Test shelter for updating a room",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear el room
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="Room to Update",
        description="Initial description",
        capacity=4,
        actual_tenant_number=0,
        availability=True,
        created_at=datetime.now()
    )
    response_create = room_controller.create_room(room_data)
    room_id = response_create.data.id

    # Actualizar el room
    update_data = models.RoomUpdate(
        id=room_id,
        id_shelter=response_shelter.data.id,
        name="Updated Room",
        description="Updated description",
        capacity=6,
        actual_tenant_number=2,
        availability=False
    )
    response = room_controller.update_room(update_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "Room successfully updated"
    updated_room = response.data
    assert updated_room.name == "Updated Room"
    assert updated_room.description == "Updated description"
    assert updated_room.capacity == 6
    assert updated_room.actual_tenant_number == 2
    assert updated_room.availability is False
