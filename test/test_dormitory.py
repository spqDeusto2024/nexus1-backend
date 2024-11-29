import pytest
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.models import *  # Tus modelos Pydantic
from app.controllers.dormitory_handler import Dormitory_Controller
from app.controllers.shelter_handler import Shelter_Controller
from mysql import TestDataBase  # Tu clase para la base de datos
import app.mysql.models as mysql_models  # El modelo SQLAlchemy de Dormitory
import app.utils.vars as var


@pytest.fixture(scope="module")
def db_session():
    """
    Fixture que crea una sesión de base de datos para las pruebas.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración
    session = db.get_session()
    yield session
    session.close()



def test_healthz():
    """
    Test para verificar el estado del controlador.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración
    controller = Dormitory_Controller(db)
    result = controller.healthz()
    assert result == {"status": "ok"}


def test_create_dormitory(db_session):
    """
    Test para crear un nuevo dormitorio.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración
    controller = Dormitory_Controller(db)
    shelter_controller = Shelter_Controller(db)
    shelter_data = ShelterCreate(name = "shelter",description = "shelter for dormitory",created_at = datetime.now())
    shelter_response = shelter_controller.create_shelter(shelter_data)

    dormitory_data = DormitoryCreate(
        id_shelter=shelter_response.data.id,
        name="New Dormitory",
        description="A new dormitory",
        capacity=20,
        actual_tenant_number=5,
        availability=True,
        created_at = datetime.now()
    )

    try:
        response = controller.create_dormitory(dormitory_data)
    except Exception as e:
        raise e
    
    print(response.message)

    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Dormitory inserted into database successfully"




def test_get_all_dormitories(db_session):
    """
    Test para obtener todos los dormitorios.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración
    controller = Dormitory_Controller(db)
    response = controller.get_all()

    assert response.status == "ok"
    assert isinstance(response.data, list)
    assert len(response.data) > 0


def test_update_dormitory(db_session):
    """
    Test para actualizar un dormitorio existente.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración
    controller = Dormitory_Controller(db)
    shelter_controller = Shelter_Controller(db)
    shelter_data = ShelterCreate(name = "shelter_update",description = "shelter for dormitory_update",created_at = datetime.now())
    shelter_response = shelter_controller.create_shelter(shelter_data)
    dormitory_data = DormitoryCreate(
        id_shelter=shelter_response.data.id,
        name="Dormitory to Update",
        description="Old description",
        capacity=20,
        actual_tenant_number=5,
        availability=True,
        created_at = datetime.now()
    )
    create_response = controller.create_dormitory(dormitory_data)

    updated_data = DormitoryUpdate(
        id=create_response.data.id,
        id_shelter = shelter_response.data.id,
        name="Updated Dormitory",
        description="New description",
        capacity=25,
        actual_tenant_number=10,
        availability=False
    )
    response = controller.update_dormitory(updated_data)

    assert response.status == "ok"
    assert response.message == "Dormitory successfully updated"

   


def test_delete_dormitory(db_session):
    """
    Test para eliminar un dormitorio.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración
    controller = Dormitory_Controller(db)
    shelter_controller = Shelter_Controller(db)
    shelter_data = ShelterCreate(name = "shelter_delete",description = "shelter for dormitory_delete",created_at = datetime.now())
    shelter_response = shelter_controller.create_shelter(shelter_data)
    dormitory_data = DormitoryCreate(
        id_shelter=shelter_response.data.id,
        name="Dormitory to Delete",
        description="Will be deleted",
        capacity=10,
        actual_tenant_number=2,
        availability=True,
        created_at = datetime.now()
    )
    create_response = controller.create_dormitory(dormitory_data)

    delete_data = DormitoryDelete(id=create_response.data.id)
    response = controller.delete_dormitory(delete_data)

    assert response.status == "ok"
    assert response.message == "Dormitory successfully deleted"

