import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class Role_Controller:
    """
    Controller for managing Role-related operations.

    This class handles the creation, updating, deletion, and retrieval of roles in the database.

    Methods:
        healhz: Checks the status of the connection.
        create_shelter: Creates a new role in the database.
        get_all: Retrieves all roles stored in the database.
        delete_shelter: Deletes a role from the database.
        update_shelter: Updates an existing role in the database.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Role_Controller class.

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

    def create_role(self, body: models.RoleCreate):
        """
        Creates a new role in the database.

        This method takes a RoleCreate object, which contains the necessary data to create a role
        and saves it to the database.

        Parameters:
            body (models.RoleCreate): An object containing the shelter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Role(name=body.name, description=body.description, id=body.id_room_relationship)
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Role inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting Role into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all Roles from the database.

        This method queries all Roles records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and Role data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.Role).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All Roles successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving Roles from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_role(self, body: models.RoleDelete):
        """
        Deletes a Role from the database.

        This method takes a RoleDelete object, which contains the ID of the Role to delete.

        Parameters:
            body (models.RoleDelete): An object containing the shelter ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted Role data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                role_deleted = session.query(mysql_models.Role).get(body.id)
                session.delete(role_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Role successfully deleted",
                data=role_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting Role from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_role(self, body: models.RoleUpdate):
        """
        Updates an existing Role in the database.

        This method takes a RoleUpdate object, which contains the updated data for the Role,
        and updates the corresponding record in the database.

        Parameters:
            body (models.RoleUpdate): An object containing the updated Role data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated  Role.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                Role: mysql_models.Role = session.query(mysql_models.Role).get(body.id)
                Role.name = body.name
                Role.description = body.description
                Role.idRoomRelationship = body.id_room_relationship
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Role successfully updated",
                data=Role,
                code=201
            )
        except Exception as e:
            print("Error updating Role in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
