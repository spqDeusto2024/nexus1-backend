import pytest
from sqlalchemy.orm import Session
from app.models.models import *  # Tus modelos Pydantic
from app.controllers.shelter_handler import Shelter_Controller  # El controlador que quieres probar
from mysql import TestDataBase  # Tu clase para la base de datos
from sqlalchemy import create_engine
import app.mysql.models as mysql_models  # El modelo SQLAlchemy de Shelter, que usas en la base de datos
import app.utils.vars as var
from datetime import datetime

# Aquí también debes agregar cualquier otro módulo que estés usando

@pytest.fixture(scope="module")
def db_session():
    # Crear una sesión de base de datos para usar en las pruebas
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    session = db.get_session()
    yield session
    session.close()

def test_healthz():
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    controller = Shelter_Controller(db)
    result = controller.healthz()
    assert result == {"status": "ok"}

def test_create_shelter(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    controller = Shelter_Controller(db)
    shelter_data = ShelterCreate(name="prove for test create shelter", description="desc for test create shelter",created_at = datetime.now())
    try:
        response = controller.create_shelter(shelter_data)
    except Exception as e:
        raise e

    
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Shelter inserted into database successfully"
    
  

def test_get_all_shelters(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    controller = Shelter_Controller(db)
    response = controller.get_all()
    
    assert response.status == "ok"
    assert isinstance(response.data, list)
    assert len(response.data) > 0

def test_update_shelter(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    controller = Shelter_Controller(db)
    shelter_data = ShelterCreate(name="Shelter to Update", description="Old description",created_at = datetime.now())
    response = controller.create_shelter(shelter_data)
    shelter_id = response.data.id

    updated_data = ShelterUpdate(id=shelter_id, name="Updated Shelter", description="New description")
    response = controller.update_shelter(updated_data)

    assert response.status == "ok"
    assert response.message == "Shelter successfully updated"


def test_delete_shelter(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    controller = Shelter_Controller(db)
    shelter_data = ShelterCreate(name="Shelter to Delete", description="Will be deleted",created_at = datetime.now())
    response = controller.create_shelter(shelter_data)
    shelter_id = response.data.id

    delete_data = ShelterDelete(id=shelter_id)
    response = controller.delete_shelter(delete_data)

    assert response.status == "ok"
    assert response.message == "Shelter successfully deleted"

   
