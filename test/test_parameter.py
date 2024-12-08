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
    # Crear una sesión de base de datos para usar en las pruebas
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    session = db.get_session()
    yield session
    session.close()

def test_create_parameter(db_session):
    """
    Prueba la creación de un nuevo `Parameter`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Parameter_Controller(db)

    # Crear el parámetro
    parameter_data = models.ParameterCreate(
        name="Test Parameter",
        description="Parameter for testing purposes",
        max_value=100.0,
        min_value=0.0,
        created_at=datetime.now()
    )
    response = controller.create_parameter(parameter_data)

    # Validar la respuesta
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Parameter inserted into database successfully"
    assert response.data is not None
    assert response.data.name == "Test Parameter"

def test_get_all_parameters(db_session):
    """
    Prueba la obtención de todos los parámetros.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Parameter_Controller(db)

    # Obtener todos los parámetros
    response = controller.get_all()

    # Validar la respuesta
    assert response.status == "ok"
    assert response.code == 200
    assert isinstance(response.data, list)

def test_delete_parameter(db_session):
    """
    Prueba la eliminación de un `Parameter`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Parameter_Controller(db)

    # Crear un parámetro para luego eliminarlo
    parameter_data = models.ParameterCreate(
        name="Parameter to Delete",
        description="This parameter will be deleted",
        max_value=50.0,
        min_value=10.0,
        created_at=datetime.now()
    )
    response_create = controller.create_parameter(parameter_data)
    parameter_id = response_create.data.id

    # Eliminar el parámetro
    delete_data = models.ParameterDelete(id=parameter_id)
    response = controller.delete_parameter(delete_data)

    # Validar la respuesta
    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "Parameter successfully deleted"

def test_update_parameter(db_session):
    """
    Prueba la actualización de un `Parameter`.
    """
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Parameter_Controller(db)

    # Crear un parámetro para luego actualizarlo
    parameter_data = models.ParameterCreate(
        name="Parameter to Update",
        description="Initial description",
        max_value=75.0,
        min_value=25.0,
        created_at=datetime.now()
    )
    response_create = controller.create_parameter(parameter_data)
    parameter_id = response_create.data.id

    # Actualizar el parámetro
    update_data = models.ParameterUpdate(
        id=parameter_id,
        name="Updated Parameter",
        description="Updated description",
        max_value=90.0,
        min_value=20.0
    )
    response = controller.update_parameter(update_data)

    # Recuperar el parámetro actualizado
    with db.get_session() as session:
        updated_parameter = session.query(mysql_models.Parameter).get(parameter_id)

    # Validar la respuesta
    assert response.status == "ok"
    assert response.code == 200
    assert response.message == "Parameter successfully updated"
    assert updated_parameter.name == "Updated Parameter"
    assert updated_parameter.description == "Updated description"
    assert updated_parameter.max_value == 90.0
    assert updated_parameter.min_value == 20.0

