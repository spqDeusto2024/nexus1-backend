import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class Tenant_Relationship_Controller:
    """
    Controller for managing tenant_relationship-related operations.

    This class handles the creation, updating, deletion, and retrieval of tenant_relationship in the database.

    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Tenant_Relationship_Controller class.

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

    def create_tenant_relationship(self, body: models.TenantRelationshipCreate):
        """
        Creates a new tenant_relationship in the database.

        This method takes a Tenant_RelationshipCreate object, which contains the necessary data to create a tenant_relationship
        and saves it to the database.

        Parameters:
            body (models.Tenant_RelationshipCreate): An object containing the tenant_relationship data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.TenantRelationship(
                id_tenant_1 = body.id_tenant_1,
                id_tenant_2 = body.id_tenant_2,
                id_relationship = body.id_relationship
            )
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant_relationship inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting tenant_relationship into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all tenant_relationship from the database.

        This method queries all tenant_relationship records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and tenant_relationship data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.TenantRelationship).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All tenant_relationships successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving tenant_relationship from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_tenantRelationship(self, body: models.TenantRelationshipDelete):
        """
        Deletes a dormitory from the database.

        This method takes a tenant_relationship object, which contains the ID of the tenant_relationship to delete.

        Parameters:
            body (models.TenantRelationshipDelete): An object containing the tenant_relationship ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted tenant_relationship data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                tenant_relationship_deleted = session.query(mysql_models.TenantRelationship).get(body.id)
                session.delete(tenant_relationship_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant_relationship successfully deleted",
                data=tenant_relationship_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting tenant_relationship from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_tenantRelationship(self, body: models.TenantRelationshipUpdate):
        """
        Updates an existing tenant_relationship in the database.

        This method takes a TenantRelationshipUpdate object, which contains the updated data for the tenant_relationship,
        and updates the corresponding record in the database.

        Parameters:
            body (models.TenantRelationshipUpdate): An object containing the updated tenant_relationship data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated tenant_relationship data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                tenantRelationship: mysql_models.TenantRelationship = session.query(mysql_models.TenantRelationship).get(body.id_tenant_relationship)
                tenantRelationship.id_tenant_1=body.id_tenant_1
                tenantRelationship.id_tenant_2=body.id_tenant_2
                tenantRelationship.id_relationship=body.id_relationship

                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant_relationship successfully updated",
                data=tenantRelationship,
                code=201
            )
        except Exception as e:
            print("Error updating tenant_relationship in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

