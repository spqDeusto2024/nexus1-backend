import pytest
from sqlalchemy.orm import Session
from datetime import datetime
from app.controllers.parameter_handler import Parameter_Controller
import app.models.models as models
import app.mysql.models as mysql_models  # Modelos SQLAlchemy
from mysql import TestDataBase  # Clase de base de datos
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

def test_healthz(db_session):
    """
    Prueba el endpoint de salud.
    """
    controller = Parameter_Controller(TestDataBase("mysql://test:test@test-database:3306/test"))
    result = controller.healthz()
    assert result == {"status": "ok"}

def test_create_parameter(db_session):
    """
    Prueba la creación de un nuevo parámetro.
    """
    controller = Parameter_Controller(TestDataBase("mysql://test:test@test-database:3306/test"))
    parameter_data = models.ParameterCreate(
        name="Test Parameter",
        description="A parameter for testing",
        created_at=datetime.now()
    )
    response = controller.create_parameter(parameter_data)

    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Parameter inserted into database successfully"

def test_get_all_parameters(db_session):
    """
    Prueba la obtención de todos los parámetros.
    """
    controller = Parameter_Controller(TestDataBase("mysql://test:test@test-database:3306/test"))
    response = controller.get_all()
    assert response.status == "ok"
    assert response.code == 200
    assert isinstance(response.data, list)
    assert len(response.data) > 0  # Se espera que haya al menos un parámetro en la base de datos

def test_update_parameter(db_session):
    """
    Prueba la actualización de un parámetro existente.
    """
    controller = Parameter_Controller(TestDataBase("mysql://test:test@test-database:3306/test"))
    # Crea un parámetro inicial para actualizar
    initial_data = models.ParameterCreate(
        name="Old Parameter",
        description="Old description",
        created_at=datetime.now()
    )
    create_response = controller.create_parameter(initial_data)

    # Actualiza el parámetro
    updated_data = models.ParameterUpdate(
        id=create_response.data.id,
        name="Updated Parameter",
        description="New description"
    )
    response = controller.update_parameter(updated_data)

    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "Parameter successfully updated"

def test_delete_parameter(db_session):
    """
    Prueba la eliminación de un parámetro.
    """
    controller = Parameter_Controller(TestDataBase("mysql://test:test@test-database:3306/test"))
    # Crea un parámetro inicial para eliminar
    parameter_data = models.ParameterCreate(
        name="Parameter to Delete",
        description="Will be deleted",
        created_at=datetime.now()
    )
    create_response = controller.create_parameter(parameter_data)

    # Elimina el parámetro
    delete_data = models.ParameterDelete(id=create_response.data.id)
    response = controller.delete_parameter(delete_data)

    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "Parameter successfully deleted"
