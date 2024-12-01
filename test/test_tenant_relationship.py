from app.controllers.tenant_relationship_handler import Tenant_Relationship_Controller
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
from app.controllers.relationship_handler import Relationship_Controller 
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

def test_create_tenant_relationship(db_session):
    """
    Prueba la creación de un nuevo `TenantRelationship`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    tenant_relationship_controller = Tenant_Relationship_Controller(db)
    tenant_controller = Tenant_Controller(db)
    relationship_controller = Relationship_Controller(db)

    # Crear un relationship con un id explícito
    relationship_data = models.RelationshipCreate(
        id=1,  # Proporcionamos manualmente un id único
        name="Friendship",
        description="Relationship type for tenants",
        created_at=datetime.now()
    )
    response_relationship = relationship_controller.create_relationship(relationship_data)

    # Crear dos tenants
    tenant_data_1 = models.TenantCreate(
        id_role=None,
        id_dormitory=None,
        name="Tenant 1",
        surname="Lastname 1",
        age="25",
        status=True,
        genre="Male",
        created_at=datetime.now()
    )
    response_tenant_1 = tenant_controller.create_tenant(tenant_data_1)

    tenant_data_2 = models.TenantCreate(
        id_role=None,
        id_dormitory=None,
        name="Tenant 2",
        surname="Lastname 2",
        age="30",
        status=True,
        genre="Female",
        created_at=datetime.now()
    )
    response_tenant_2 = tenant_controller.create_tenant(tenant_data_2)

    # Crear tenant relationship
    tenant_relationship_data = models.TenantRelationshipCreate(
        id_tenant_1=response_tenant_1.data.id,
        id_tenant_2=response_tenant_2.data.id,
        id_relationship=response_relationship.data.id,
        created_at=datetime.now()
    )
    response_create = tenant_relationship_controller.create_tenant_relationship(tenant_relationship_data)

    # Validar que la relación fue creada y obtener el ID
    assert response_create.status == "ok"
    tenant_relationship_id = response_create.data.id_tenant_relationship  # Usamos id_tenant_relationship
    assert tenant_relationship_id is not None

    # Validaciones adicionales
    assert response_create.code == 201
    assert response_create.message == "Tenant_relationship inserted into database successfully"

def test_get_all_tenant_relationships(db_session):
    """
    Prueba la obtención de todas las relaciones entre tenants.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    tenant_relationship_controller = Tenant_Relationship_Controller(db)

    # Obtener todas las relaciones
    response = tenant_relationship_controller.get_all()

    # Validaciones
    assert response.status == "ok"
    assert isinstance(response.data, list)

def test_delete_tenant_relationship(db_session):
    """
    Prueba la eliminación de un `TenantRelationship`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    tenant_relationship_controller = Tenant_Relationship_Controller(db)
    tenant_controller = Tenant_Controller(db)
    relationship_controller = Relationship_Controller(db)

    # Crear un relationship con id explícito
    relationship_data = models.RelationshipCreate(
        id=2,  # Proporcionamos un id único
        name="Family",
        description="Relationship type for deletion test",
        created_at=datetime.now()
    )
    response_relationship = relationship_controller.create_relationship(relationship_data)

    # Crear dos tenants
    tenant_data_1 = models.TenantCreate(
        id_role=None,
        id_dormitory=None,
        name="Tenant Delete 1",
        surname="Lastname Delete 1",
        age="28",
        status=True,
        genre="Male",
        created_at=datetime.now()
    )
    response_tenant_1 = tenant_controller.create_tenant(tenant_data_1)

    tenant_data_2 = models.TenantCreate(
        id_role=None,
        id_dormitory=None,
        name="Tenant Delete 2",
        surname="Lastname Delete 2",
        age="32",
        status=True,
        genre="Female",
        created_at=datetime.now()
    )
    response_tenant_2 = tenant_controller.create_tenant(tenant_data_2)

    # Crear tenant relationship
    tenant_relationship_data = models.TenantRelationshipCreate(
        id_tenant_1=response_tenant_1.data.id,
        id_tenant_2=response_tenant_2.data.id,
        id_relationship=response_relationship.data.id,
        created_at=datetime.now()
    )
    response_create = tenant_relationship_controller.create_tenant_relationship(tenant_relationship_data)

    # Validar que la relación fue creada y obtener el ID
    assert response_create.status == "ok"
    tenant_relationship_id = response_create.data.id_tenant_relationship  # Usamos id_tenant_relationship

    # Eliminar la relación
    delete_data = models.TenantRelationshipDelete(
        id_tenant_relationship=tenant_relationship_id
    )
    response = tenant_relationship_controller.delete_tenant_relationship(delete_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Tenant_relationship successfully deleted"

def test_update_tenant_relationship(db_session):
    """
    Prueba la actualización de un `TenantRelationship`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    tenant_relationship_controller = Tenant_Relationship_Controller(db)
    tenant_controller = Tenant_Controller(db)
    relationship_controller = Relationship_Controller(db)

    # Crear un relationship inicial con id explícito
    relationship_data_1 = models.RelationshipCreate(
        id=3,  # Proporcionamos un id único
        name="Colleague",
        description="Initial relationship type",
        created_at=datetime.now()
    )
    response_relationship_1 = relationship_controller.create_relationship(relationship_data_1)

    # Crear un relationship nuevo para actualizar con id explícito
    relationship_data_2 = models.RelationshipCreate(
        id=4,  # Proporcionamos un id único
        name="Roommate",
        description="Updated relationship type",
        created_at=datetime.now()
    )
    response_relationship_2 = relationship_controller.create_relationship(relationship_data_2)

    # Crear dos tenants
    tenant_data_1 = models.TenantCreate(
        id_role=None,
        id_dormitory=None,
        name="Tenant Update 1",
        surname="Lastname Update 1",
        age="35",
        status=True,
        genre="Male",
        created_at=datetime.now()
    )
    response_tenant_1 = tenant_controller.create_tenant(tenant_data_1)

    tenant_data_2 = models.TenantCreate(
        id_role=None,
        id_dormitory=None,
        name="Tenant Update 2",
        surname="Lastname Update 2",
        age="40",
        status=True,
        genre="Female",
        created_at=datetime.now()
    )
    response_tenant_2 = tenant_controller.create_tenant(tenant_data_2)

    # Crear tenant relationship
    tenant_relationship_data = models.TenantRelationshipCreate(
        id_tenant_1=response_tenant_1.data.id,
        id_tenant_2=response_tenant_2.data.id,
        id_relationship=response_relationship_1.data.id,
        created_at=datetime.now()
    )
    response_create = tenant_relationship_controller.create_tenant_relationship(tenant_relationship_data)

    # Validar que la relación fue creada y obtener el ID
    assert response_create.status == "ok"
    tenant_relationship_id = response_create.data.id_tenant_relationship  # Usamos id_tenant_relationship

    # Actualizar tenant relationship
    update_data = models.TenantRelationshipUpdate(
        id_tenant_relationship=tenant_relationship_id,
        id_tenant_1=response_tenant_1.data.id,
        id_tenant_2=response_tenant_2.data.id,
        id_relationship=response_relationship_2.data.id
    )
    response = tenant_relationship_controller.update_tenant_relationship(update_data)

    # Validaciones
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Tenant_relationship successfully updated"
