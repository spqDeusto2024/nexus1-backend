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

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the Tenant_Relationship_Controller class.

        Parameters:
            db (object): An instance of a database (e.g., Nexus1DataBase) that will be used to create the database connection.
        """
        self.db = db  # Ya se pasa directamente la instancia de la base de datos
    
    def healthz(self):
        """
        Checks the status of the connection.

        Returns:
            dict: A dictionary with the status "ok".
        """
        return {"status": "ok"}

    def create_tenant_relationship(self, body: models.TenantRelationshipCreate):
        """
        Creates a new tenant_relationship in the database.

        Parameters:
            body (models.Tenant_RelationshipCreate): An object containing the tenant_relationship data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.TenantRelationship(
                id_tenant_1=body.id_tenant_1,
                id_tenant_2=body.id_tenant_2,
                id_relationship=body.id_relationship
            )
            with Session(self.db.engine) as session:  # Usamos self.db directamente
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

        Returns:
            ResponseModel: A response model with the status of the operation, message, and tenant_relationship data.
        """
        try:
            response: list = []
            with Session(self.db.engine) as session:  # Usamos self.db directamente
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

    def delete_tenant_relationship(self, body: models.TenantRelationshipDelete):
        """
        Deletes a tenant_relationship from the database.

        Parameters:
            body (models.TenantRelationshipDelete): An object containing the tenant_relationship ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted tenant_relationship data.
        """
        try:
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                tenant_relationship_deleted = session.query(mysql_models.TenantRelationship).get(body.id_tenant_relationship)
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

    def update_tenant_relationship(self, body: models.TenantRelationshipUpdate):
        """
        Updates an existing tenant_relationship in the database.

        Parameters:
            body (models.TenantRelationshipUpdate): An object containing the updated tenant_relationship data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated tenant_relationship data.
        """
        try:
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                tenant_relationship: mysql_models.TenantRelationship = session.query(mysql_models.TenantRelationship).get(body.id_tenant_relationship)
                tenant_relationship.id_tenant_1 = body.id_tenant_1
                tenant_relationship.id_tenant_2 = body.id_tenant_2
                tenant_relationship.id_relationship = body.id_relationship

                session.dirty  # La sesión se marca como sucia automáticamente
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant_relationship successfully updated",
                data=tenant_relationship,
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
