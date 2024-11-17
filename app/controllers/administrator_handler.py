import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase
from app.utils.hashing import verify_password,hash_password

import app.utils.vars as var
from sqlalchemy.orm import Session

class Administrator_Controller:
    """
    Controller for managing administrator-related operations.

    This class handles the creation, updating, deletion, retrieval, and authentication of administrators in the database.

    
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Administrator_Controller class.
        """
        pass
    
    def healthz(self):
        """
        Checks the status of the connection.

        Returns:
            dict: A dictionary with the status "ok".
        """
        return {"status": "ok"}

    def create_administrator(self, body: models.AdministratorCreate):
        """
        Creates a new administrator in the database.

        Parameters:
            body (models.AdministratorCreate): An object containing the administrator data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Administrator(username=body.username, password=hash_password(body.password))
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Administrator inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting administrator into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all administrators from the database.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and administrator data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.Administrator).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All administrators successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving administrators from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_administrator(self, body: models.AdministratorDelete):
        """
        Deletes an administrator from the database.

        Parameters:
            body (models.AdministratorDelete): An object containing the administrator ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted administrator data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                administrator_deleted = session.query(mysql_models.Administrator).get(body.id)
                session.delete(administrator_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Administrator successfully deleted",
                data=administrator_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting administrator from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_administrator(self, body: models.AdministratorUpdate):
        """
        Updates an existing administrator in the database.

        Parameters:
            body (models.AdministratorUpdate): An object containing the updated administrator data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated administrator data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                administrator: mysql_models.Administrator = session.query(mysql_models.Administrator).get(body.id)
                administrator.username = body.username
                administrator.password = body.password
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Administrator successfully updated",
                data=administrator,
                code=201
            )
        except Exception as e:
            print("Error updating administrator in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_admin_by_username(self, username: str):
        """
        Retrieves an administrator by their username.

        This method queries the database for an administrator based on the provided username and returns the details.

        Parameters:
            username (str): The username of the administrator to retrieve.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and administrator data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                admin = session.query(mysql_models.Administrator).filter_by(username=username).first()
                session.close()

            if admin:
                return ResponseModel(
                    status="ok",
                    message="Administrator retrieved successfully",
                    data=admin,
                    code=200
                )
            else:
                return ResponseModel(
                    status="error",
                    message="Administrator not found",
                    data=None,
                    code=404
                )
        except Exception as e:
            print(f"Error retrieving administrator by username: {str(e)}")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )