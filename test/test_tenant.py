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
from app.controllers.tenant_handler import Tenant_Controller  # Controlador de tenants
from app.controllers.role_handler import Role_Controller  # Controlador de roles
from app.controllers.dormitory_handler import Dormitory_Controller
import app.models.models as models

@pytest.fixture(scope="module")
def db_session():
    # Crear una sesión de base de datos para usar en las pruebas
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta según tu configuración
    session = db.get_session()
    yield session
    session.close()


def test_create_tenant(db_session):
    """
    Prueba la creación de un nuevo `Tenant`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    tenant_controller = Tenant_Controller(db)
    role_controller = Role_Controller(db)
    dormitory_controller = Dormitory_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Test Shelter",
        description="Shelter for dormitory testing",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un role
    role_data = models.RoleCreate(
        name="Tenant Role",
        description="Role for tenant testing",
        created_at=datetime.now()
    )
    response_role = role_controller.create_role(role_data)

    # Crear un dormitory asociado al shelter
    dormitory_data = models.DormitoryCreate(
        id_shelter=response_shelter.data.id,
        name="Test Dormitory",
        description="Dormitory for tenant testing",
        capacity=10,
        created_at=datetime.now()
    )
    response_dormitory = dormitory_controller.create_dormitory(dormitory_data)

    # Crear un tenant asociado al role y dormitory
    tenant_data = models.TenantCreate(
        id_role=response_role.data.id,
        id_dormitory=response_dormitory.data.id,
        name="John",
        surname="Doe",
        age="30",
        status=True,
        genre="Male",
        created_at=datetime.now()
    )
    response = tenant_controller.create_tenant(tenant_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Tenant inserted into database successfully"


def test_delete_tenant(db_session):
    """
    Prueba la eliminación de un `Tenant`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    tenant_controller = Tenant_Controller(db)
    role_controller = Role_Controller(db)
    dormitory_controller = Dormitory_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Delete Tenant Shelter",
        description="Shelter for delete tenant test",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un role
    role_data = models.RoleCreate(
        name="Delete Tenant Role",
        description="Role for delete tenant test",
        created_at=datetime.now()
    )
    response_role = role_controller.create_role(role_data)

    # Crear un dormitory asociado al shelter
    dormitory_data = models.DormitoryCreate(
        id_shelter=response_shelter.data.id,
        name="Delete Tenant Dormitory",
        description="Dormitory for delete tenant test",
        capacity=5,
        created_at=datetime.now()
    )
    response_dormitory = dormitory_controller.create_dormitory(dormitory_data)

    # Crear un tenant asociado al role y dormitory
    tenant_data = models.TenantCreate(
        id_role=response_role.data.id,
        id_dormitory=response_dormitory.data.id,
        name="Jane",
        surname="Smith",
        age="25",
        status=True,
        genre="Female",
        created_at=datetime.now()
    )
    response_create = tenant_controller.create_tenant(tenant_data)
    tenant_id = response_create.data.id

    # Intentar eliminar el tenant
    delete_data = models.TenantDelete(id=tenant_id)
    response = tenant_controller.delete_tenant(delete_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Tenant successfully deleted"


def test_update_tenant(db_session):
    """
    Prueba la actualización de un `Tenant`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    tenant_controller = Tenant_Controller(db)
    role_controller = Role_Controller(db)
    dormitory_controller = Dormitory_Controller(db)
    shelter_controller = Shelter_Controller(db)

    # Crear un shelter
    shelter_data = models.ShelterCreate(
        name="Update Tenant Shelter",
        description="Shelter for update tenant test",
        created_at=datetime.now()
    )
    response_shelter = shelter_controller.create_shelter(shelter_data)

    # Crear un role
    role_data = models.RoleCreate(
        name="Update Tenant Role",
        description="Role for update tenant test",
        created_at=datetime.now()
    )
    response_role = role_controller.create_role(role_data)

    # Crear un dormitory asociado al shelter
    dormitory_data = models.DormitoryCreate(
        id_shelter=response_shelter.data.id,
        name="Update Tenant Dormitory",
        description="Dormitory for update tenant test",
        capacity=8,
        created_at=datetime.now()
    )
    response_dormitory = dormitory_controller.create_dormitory(dormitory_data)

    # Crear un tenant asociado al role y dormitory
    tenant_data = models.TenantCreate(
        id_role=response_role.data.id,
        id_dormitory=response_dormitory.data.id,
        name="Mark",
        surname="Taylor",
        age="40",
        status=True,
        genre="Male",
        created_at=datetime.now()
    )
    response_create = tenant_controller.create_tenant(tenant_data)
    tenant_id = response_create.data.id

    # Actualizar el tenant
    update_data = models.TenantUpdate(
        id=tenant_id,
        name="Updated Mark",
        surname="Updated Taylor",
        age="45",
        status=False,
        genre="Male"
    )
    response = tenant_controller.update_tenant(update_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Tenant successfully updated"
