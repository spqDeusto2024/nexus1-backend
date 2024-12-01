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

def test_create_role(db_session):
    """
    Prueba la creación de un nuevo `Role`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Role_Controller(db)
    shelter_controller = Shelter_Controller(db)  # Correcto
    room_controller = Room_Controller(db)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Test Shelter for Role",
        description="Shelter for role testing",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un room asociado al shelter
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="Test Room for Role",
        created_at=datetime.now()
    )
    response_room = room_controller.create_room(room_data)

    # Crear un role asociado al room
    role_data = models.RoleCreate(
        name="Test Role",
        description="Role description for testing",
        id_room_relationship=response_room.data.id,
        created_at=datetime.now()
    )
    response = controller.create_role(role_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Role inserted into database successfully"

def test_get_all_roles(db_session):
    """
    Prueba la obtención de todos los `Roles`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Role_Controller(db)

    # Intentar recuperar todos los roles
    response = controller.get_all()
    print(response)

    # Validaciones
    assert response.status == "ok"
    assert isinstance(response.data, list)

def test_delete_role(db_session):
    """
    Prueba la eliminación de un `Role`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Role_Controller(db)
    shelter_controller = Shelter_Controller(db)  # Correcto
    room_controller = Room_Controller(db)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Delete Role Shelter",
        description="Shelter for delete role test",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un room asociado al shelter
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="Delete Role Room",
        created_at=datetime.now()
    )
    response_room = room_controller.create_room(room_data)

    # Crear un role asociado al room
    role_data = models.RoleCreate(
        name="Delete Role",
        description="Role for delete test",
        id_room_relationship=response_room.data.id,
        created_at=datetime.now()
    )
    response_create = controller.create_role(role_data)
    role_id = response_create.data.id

    # Intentar eliminar el rol
    delete_data = models.RoleDelete(id=role_id)
    response = controller.delete_role(delete_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Role successfully deleted"

def test_update_role(db_session):
    """
    Prueba la actualización de un `Role`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Role_Controller(db)
    shelter_controller = Shelter_Controller(db)  # Correcto
    room_controller = Room_Controller(db)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Update Role Shelter",
        description="Shelter for update role test",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un room asociado al shelter
    room_data = models.RoomCreate(
        id_shelter=response_shelter.data.id,
        name="Update Role Room",
        created_at=datetime.now()
    )
    response_room = room_controller.create_room(room_data)

    # Crear un role asociado al room
    role_data = models.RoleCreate(
        name="Old Role",
        description="Role for update test",
        id_room_relationship=response_room.data.id,
        created_at=datetime.now()
    )
    response_create = controller.create_role(role_data)
    role_id = response_create.data.id

    # Actualizar el role
    update_data = models.RoleUpdate(
        id=role_id,
        name="Updated Role",
        description="Updated role description",
        id_room_relationship=response_room.data.id
    )
    response = controller.update_role(update_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Role successfully updated"
