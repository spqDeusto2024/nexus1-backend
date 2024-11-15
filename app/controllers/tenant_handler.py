import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session

class Tenant_Controller:
    """
    Controller for managing tenant-related operations.

    This class handles the creation, updating, deletion, and retrieval of tenants in the database.

    Methods:
        healhz: Checks the status of the connection.
        create_tenant: Creates a new tenant in the database.
        get_all: Retrieves all tenants stored in the database.
        delete_tenant: Deletes a tenant from the database.
        update_tenant: Updates an existing tenant in the database.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Tenant_Controller class.

        This constructor does not take any parameters and does not perform any operation.
        """
        pass
    
    def healthz(self):
        """
        Checks the status of the connection.

        This method returns a "ok" status message indicating that the API is working correctly.

        Returns:
            dict: A dictionary with the status "ok".
        """
        return {"status": "ok"}

    def create_tenant(self, body: models.TenantCreate):
        """
        Creates a new tenant in the database.

        This method takes a TenantCreate object, which contains the necessary data to create a tenant
        and saves it to the database.

        Parameters:
            body (models.TenantCreate): An object containing the tenant data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Tenant(
                id_role = body.id_shelter,
                id_dormitory = body.id_dormitory,
                name = body.name,
                surname = body.surname, 
                age = body.age,
                status = body.status,
                genre = body.genre
                
            )
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting tenant into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all tenants from the database.

        This method queries all tenant records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and tenant data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.Tenant).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All tenants successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving tenants from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_tenant(self, body: models.TenantDelete):
        """
        Deletes a tenant from the database.

        This method takes a TenantDelete object, which contains the ID of the tenant to delete.

        Parameters:
            body (models.TenantDelete): An object containing the tenant ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted tenant data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                tenant_deleted = session.query(mysql_models.Dormitory).get(body.id)
                session.delete(tenant_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant successfully deleted",
                data=tenant_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting tenant from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_tenant(self, body: models.TenantUpdate):
        """
        Updates an existing tenant in the database.

        This method takes a TenantUpdate object, which contains the updated data for the tenant,
        and updates the corresponding record in the database.

        Parameters:
            body (models.TenantUpdate): An object containing the updated tenant data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated tenant data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                tenant:mysql_models.Tenant = session.query(mysql_models.Tenant).get(body.id)
                tenant.name = body.name
                tenant.surname = body.surname
                tenant.age = body.age
                tenant.status= body.status
                tenant.genre = body.genre
                
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant successfully updated",
                data=dormitory,
                code=201
            )
        except Exception as e:
            print("Error updating tenant in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

