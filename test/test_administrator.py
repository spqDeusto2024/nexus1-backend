import pytest
from sqlalchemy.orm import Session
from app.models.models import *  # Tus modelos Pydantic
from app.controllers.administrator_handler import Administrator_Controller  # El controlador que quieres probar
from mysql import TestDataBase  # Tu clase para la base de datos
from sqlalchemy import create_engine
import app.mysql.models as mysql_models  # El modelo SQLAlchemy de Shelter, que usas en la base de datos
import app.utils.vars as var
from datetime import datetime
from app.utils.hashing import hash_password



@pytest.fixture(scope="module")
def db_session():
    # Crear una sesión de base de datos para usar en las pruebas
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    session = db.get_session()
    yield session
    session.close()




def test_create_administrator(db_session):
    # Usamos una base de datos de pruebas (configurar adecuadamente el URL de conexión)
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Ajusta esto según tu configuración de base de datos
    controller = Administrator_Controller(db)

    # Creamos los datos del administrador
    admin_data = AdministratorCreate(username="testadmin", password="password123",created_at = datetime.now())

    try:
        # Intentamos crear el administrador en la base de datos
        response = controller.create_administrator(admin_data)
        print(response)
    except Exception as e:
        raise e

    # Validamos que la respuesta sea la esperada
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Administrator inserted into database successfully"


def test_get_all_administrators(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Administrator_Controller(db)
   
    # Creamos los datos del administrador
    admin_data = AdministratorCreate(username="testadmin", password="password123",created_at = datetime.now())

    try:
        response = controller.get_all()
        print(response)
    except Exception as e:
        raise e

    # Validamos que se obtuvieron los administradores
    assert response.status == "ok"
    assert isinstance(response.data, list)


def test_delete_administrator(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Administrator_Controller(db)

    # Creamos el administrador para poder eliminarlo después
    admin_data = AdministratorCreate(username="deleteadmin", password="password123",created_at = datetime.now())
    response_create = controller.create_administrator(admin_data)
    admin_id = response_create.data.id  # Suponiendo que la respuesta contiene el ID del nuevo administrador

    # Creamos el objeto para eliminar
    delete_data = AdministratorDelete(id=admin_id)

    try:
        # Intentamos eliminar el administrador
        response = controller.delete_administrator(delete_data)
        print(response)
    except Exception as e:
        raise e

    # Validamos que la eliminación fue exitosa
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Administrator successfully deleted"


def test_update_administrator(db_session):
    db = TestDataBase("mysql://test:test@test-database:3306/test")
    controller = Administrator_Controller(db)

    # Creamos el administrador
    admin_data = AdministratorCreate(username="updateadmin", password="password123", created_at=datetime.now())
    response_create = controller.create_administrator(admin_data)
    admin_id = response_create.data.id  # Suponiendo que la respuesta contiene el ID del nuevo administrador

    # Datos actualizados para el administrador
    update_data = AdministratorUpdate(id=admin_id, username="updatedadmin", password="newpassword123")

    try:
        # Intentamos actualizar el administrador
        response = controller.update_administrator(update_data)
        print(response)

        # Recuperamos el administrador actualizado
        response_get = controller.get_admin_by_username("updatedadmin")
        updated_admin = response_get.data  # Recuperamos el objeto administrador actualizado
    except Exception as e:
        raise e

    # Validamos que la actualización fue exitosa
    assert response.status == "ok"
    assert response.code == 201
    assert response.message == "Administrator successfully updated"
    assert updated_admin.username == "updatedadmin"  # Validamos con el administrador actualizado



def test_get_admin_by_username():
    db = TestDataBase("mysql://test:test@test-database:3306/test")  # Base de datos de prueba
    controller = Administrator_Controller(db)

    # Creamos un nuevo administrador para probar
    admin_data = AdministratorCreate(username="prueba", password="salvaje",created_at = datetime.now())
    response_create = controller.create_administrator(admin_data)
    
    # Verificamos que la creación fue exitosa
    assert response_create.status == "ok"
    assert response_create.code == 201
    assert response_create.message == "Administrator inserted into database successfully"

    # Ahora intentamos recuperar al administrador por su nombre de usuario
    response_get = controller.get_admin_by_username("testadmin")

    # Verificamos que la respuesta es correcta
    assert response_get.status == "ok"
    assert response_get.code == 200
    assert response_get.message == "Administrator retrieved successfully"

    # Comprobamos que los datos recuperados son correctos
    assert response_get.data.username == "testadmin"
    assert response_get.data.password != "testpassword123"  # Aseguramos que la contraseña está cifrada
    assert response_get.data.id is not None  # Verificamos que el ID esté presente

    # Intentamos recuperar un administrador que no existe
    response_get_nonexistent = controller.get_admin_by_username("nonexistentuser")

    # Verificamos que la respuesta es la esperada para un usuario no existente
    assert response_get_nonexistent.status == "error"
    assert response_get_nonexistent.code == 404
    assert response_get_nonexistent.message == "Administrator not found"
