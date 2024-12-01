import pytest
from sqlalchemy.orm import Session
from app.models.models import *  # Modelos Pydantic
from app.controllers.relationship_handler import Relationship_Controller  # El controlador de relaciones
from mysql import TestDataBase  # Clase para la base de datos de pruebas
from sqlalchemy import create_engine
import app.mysql.models as mysql_models  # Modelo SQLAlchemy de Relationship
import app.utils.vars as var
from datetime import datetime

@pytest.fixture(scope="module")
def db_session():
    # Crear una sesión de base de datos para usar en las pruebas
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    session = db.get_session()
    yield session
    session.close()

def test_create_relationship(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Base de datos de prueba
    controller = Relationship_Controller(db)

    # Crear datos para una nueva relación
    relationship_data = RelationshipCreate(
        id=1,
        name="Test Relationship",
        description="Test description",
        created_at=datetime.now()
    )

    try:
        # Intentamos crear la relación en la base de datos
        response = controller.create_relationship(relationship_data)
        print(response)
    except Exception as e:
        raise e

    # Validamos que la respuesta sea correcta
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Relationship inserted into database successfully"

def test_get_all_relationships(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Relationship_Controller(db)

    try:
        # Recuperamos todas las relaciones
        response = controller.get_all()
        print(response)
    except Exception as e:
        raise e

    # Validamos que se obtuvieron las relaciones
    assert response.status == "ok"
    assert isinstance(response.data, list)

def test_delete_relationship(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Relationship_Controller(db)

    # Crear una nueva relación para luego eliminarla
    relationship_data = RelationshipCreate(
        id=2,
        name="Delete Relationship",
        description="To be deleted",
        created_at=datetime.now()
    )
    response_create = controller.create_relationship(relationship_data)
    relationship_id = response_create.data.id  # Suponiendo que la respuesta contiene el ID de la relación

    # Datos para eliminar
    delete_data = RelationshipDelete(id=relationship_id)

    try:
        # Intentamos eliminar la relación
        response = controller.delete_relationship(delete_data)
        print(response)
    except Exception as e:
        raise e

    # Validamos que la eliminación fue exitosa
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Relationship successfully deleted"

def test_update_relationship(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Relationship_Controller(db)

    # Crear una relación para actualizarla
    relationship_data = RelationshipCreate(
        id=3,
        name="Old Relationship",
        description="Old description",
        created_at=datetime.now()
    )
    response_create = controller.create_relationship(relationship_data)
    relationship_id = response_create.data.id  # Suponiendo que la respuesta contiene el ID de la relación

    # Datos actualizados
    update_data = RelationshipUpdate(
        id=relationship_id,
        name="Updated Relationship",
        description="Updated description"
    )

    try:
        # Intentamos actualizar la relación
        response = controller.update_relationship(update_data)
        print(response)
    except Exception as e:
        raise e

    # Validamos que la actualización fue exitosa
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Relationship successfully updated"

