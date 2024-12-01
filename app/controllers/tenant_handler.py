import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from sqlalchemy.orm import Session

class Tenant_Controller:
    """
    Controller for managing tenant-related operations.

    This class handles the creation, updating, deletion, and retrieval of tenants in the database.
    """

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the Tenant_Controller class with a database connection.

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

    def create_tenant(self, body: models.TenantCreate):
        """
        Creates a new tenant in the database.

        Parameters:
            body (models.TenantCreate): An object containing the tenant data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Tenant(
                id_role=body.id_role,
                id_dormitory=body.id_dormitory,
                name=body.name,
                surname=body.surname,
                age=body.age,
                status=body.status,
                genre=body.genre
            )
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                session.add(body_row)
                session.commit()
                session.refresh(body_row)
                session.close()
            return ResponseModel(
                status="ok",
                message="Tenant inserted into database successfully",
                data=body_row,
                code=201
            )
        except Exception as e:
            print("Error inserting tenant into database:", e)
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all tenants from the database.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and tenant data.
        """
        try:
            response: list = []
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                response = session.query(mysql_models.Tenant).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All tenants successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving tenants from database:", e)
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_tenant(self, body: models.TenantDelete):
        """
        Deletes a tenant from the database.

        Parameters:
            body (models.TenantDelete): An object containing the tenant ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted tenant data.
        """
        try:
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                tenant_deleted = session.query(mysql_models.Tenant).get(body.id)
                if tenant_deleted:
                    session.delete(tenant_deleted)
                    session.commit()
                    session.close()
                    return ResponseModel(
                        status="ok",
                        message="Tenant successfully deleted",
                        data=tenant_deleted,
                        code=201
                    )
                else:
                    return ResponseModel(
                        status="error",
                        message="Tenant not found",
                        data=None,
                        code=404
                    )
        except Exception as e:
            print("Error deleting tenant from database:", e)
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_tenant(self, body: models.TenantUpdate):
        """
        Updates an existing tenant in the database.

        Parameters:
            body (models.TenantUpdate): An object containing the updated tenant data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated tenant data.
        """
        try:
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                tenant = session.query(mysql_models.Tenant).get(body.id)
                if tenant:
                    tenant.name = body.name
                    tenant.surname = body.surname
                    tenant.age = body.age
                    tenant.status = body.status
                    tenant.genre = body.genre

                    session.commit()
                    session.close()
                    return ResponseModel(
                        status="ok",
                        message="Tenant successfully updated",
                        data=tenant,
                        code=201
                    )
                else:
                    return ResponseModel(
                        status="error",
                        message="Tenant not found",
                        data=None,
                        code=404
                    )
        except Exception as e:
            print("Error updating tenant in database:", e)
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
