import pytest
from unittest.mock import patch, MagicMock
from app.controllers.tenant_handler import Tenant_Controller
from app.models.models import TenantCreate, TenantDelete, TenantUpdate
from app.models.response_models import ResponseModel
from datetime import datetime

@pytest.fixture
def controller():
    """Fixture to initialize the controller."""
    return Tenant_Controller()


@patch('app.controllers.tenant_handler.Tenant_Controller.healthz', return_value={"status": "ok"})
def test_healthz(mock_healthz, controller):
    """Test for the healthz method."""
    response = controller.healthz()
    assert response == {"status": "ok"}


@patch('app.controllers.tenant_handler.Tenant_Controller.create_Tenant')
def test_create_tenant(mock_create, controller):
    """Test for the create_tenant method."""
    # Simula la respuesta de create_tenant
    mock_response = ResponseModel(
        status="ok",
        message="Tenant inserted into database successfully",
        data=None,
        code=201
    )
    mock_create.return_value = mock_response  # Aquí usamos el objeto real de ResponseModel.

    # Llama al método con datos de prueba
    body = TenantCreate(
        id_role= 1,
        id_dormitory= 1,
        name= "Josu",
        surname= "Joxow",
        age= "22",
        status= True,
        genre="Male",
        created_at= datetime.now()  
    )
    response = controller.create_tenant(body)

    # Assertions para verificar que la respuesta es correcta
    assert response.status == "ok"
    assert response.message == "Tenant inserted into database successfully"
    assert response.data is None
    assert response.code == 201


@patch('app.controllers.tenant_handler.Tenant_Controller.get_all')
def test_get_all(mock_get_all, controller):
    """Test for the get_all method."""
    # Mock the response of get_all

    mock_tenants = [
        MagicMock(name="Dormitory A", id_shelter=1, capacity=100),
        MagicMock(name="Dormitory B", id_shelter=2, capacity=200),
    ]

    mock_response = ResponseModel(
        status="ok",
        message="All tenants successfully retrieved",
        data=mock_tenants,
        code=201
    )
    
    mock_get_all.return_value = mock_response
    response = controller.get_all()
    
    # Assertions
    assert response.status == "ok"
    assert response.message == "All tenants successfully retrieved"
    assert len(response.data) == 2


@patch('app.controllers.tenant_handler.Tenant_Controller.delete_tenant')
def test_delete_tenant(mock_delete, controller):
    """Test for the delete_tenant method."""
    
    # Mock the response of delete_tenant
    mock_response = ResponseModel(
        status="ok",
        message="Tenant successfully deleted",
        data=None,
        code=200
    )
    mock_delete.return_value = mock_response
    
    # Prepare the body for the delete request
    body = TenantDelete(id=1)
    
    # Call the method
    response = controller.delete_tenant(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Tenant successfully deleted"


@patch('app.controllers.tenant_handler.Tenant_Controller.update_tenant')
def test_update_tenant(mock_update, controller):
    """Test for the update_tenant method."""
    
    # Mock the response of update_dormitory
    mock_response = ResponseModel(
        status="ok",
        message="Tenant successfully updated",
        data=None,
        code=200
    )
    mock_update.return_value = mock_response
    
    # Prepare the body for the update request
    body = TenantUpdate(
        id_role= 1,
        id_dormitory= 1,
        name= "Updated name",
        surname= "Updated surname",
        age= "Updated age",
        status= True,
        genre= "Updated genre",
        id= 1 
    )
    
    # Call the method
    response = controller.update_tenant(body)

    # Assertions
    assert response.status == "ok"
    assert response.message == "Tenant successfully updated"




#Test para excepciones
@patch('app.controllers.tenant_handler.Tenant_Controller.create_tenant')
def test_create_tenant_database_error(mock_create, controller):
    """Test for create_tenant handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Database connection failed",
        data=None,
        code=500
    )
    mock_create.return_value = mock_response

    # Prepara datos de prueba
    body = TenantCreate(
        id_role= 1,
        id_dormitory= 1,
        name= "Josu",
        surname= "Joxow",
        age= "22",
        status= True,
        genre= "Male",
        created_at= datetime.now() 
    )

    # Llama al método
    response = controller.create_tenant(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Database connection failed"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.tenant_handler.Tenant_Controller.get_all')
def test_get_all_database_error(mock_get_all, controller):
    """Test for get_all handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to retrieve tenants from database",
        data=None,
        code=500
    )
    mock_get_all.return_value = mock_response

    # Llama al método
    response = controller.get_all()

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to retrieve tenants from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.tenant_handler.Tenant_Controller.delete_tenant')
def test_delete_tenant_database_error(mock_delete, controller):
    """Test for delete_tenant handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to delete tenant from database",
        data=None,
        code=500
    )
    mock_delete.return_value = mock_response

    # Prepara el body para la solicitud de eliminación
    body = DormitoryDelete(id=999)  # Un ID inexistente

    # Llama al método
    response = controller.delete_tenant(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to delete tenant from database"
    assert response.data is None
    assert response.code == 500

@patch('app.controllers.tenant_handler.Tenant_Controller.update_tenant')
def test_update_tenant_database_error(mock_update, controller):
    """Test for update_tenant handling a database error."""
    # Simula una respuesta de error
    mock_response = ResponseModel(
        status="error",
        message="Failed to update tenant in database",
        data=None,
        code=500
    )
    mock_update.return_value = mock_response

    # Prepara datos de prueba
    body = TenantUpdate(
       
        id_role= 1,
        id_dormitory= 1,
        name= "Updated name",
        surname= "Updated surname",
        age= "Updated age",
        status= True,
        genre= "Updated genre",
        id= 999
       
    )

    # Llama al método
    response = controller.update_tenant(body)

    # Validaciones
    assert response.status == "error"
    assert response.message == "Failed to update tenant in database"
    assert response.data is None
    assert response.code == 500

