import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class ParameterRoom_Controller:
    """
    Controller for managing ParameterRoom-related operations.

    This class handles the creation, updating, deletion, and retrieval of ParameterRooms in the database.

    Methods:
        healhz: Checks the status of the connection.
        create_ParameterRoom: Creates a new ParameterRoom in the database.
        get_all: Retrieves all ParameterRooms stored in the database.
        delete_ParameterRoom: Deletes a ParameterRoom from the database.
        update_ParameterRooM: Updates an existing ParameterRoom in the database.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the ParameterRoom_Controller class.

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

    def create_parameterRoom(self, body: models.ParameterRoomCreate):
        """
        Creates a new ParameterRoom in the database.

        This method takes a ParameterRoom object, which contains the necessary data to create a role
        and saves it to the database.

        Parameters:
            body (models.ParameterRoom): An object containing the shelter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.ParameterRoom(id_room = body.id_room, id_parameter= body.id_parameter, date = body.date, value = body.value)
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="ParameterRoom inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting ParameterRoom into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all ParameterRooms from the database.

        This method queries all ParameterRooms records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and ParameterRoom data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.ParameterRoom).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All ParametersRooms successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving ParametersRooms from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_ParameterRoom(self, body: models.ParameterRoomDelete):
        """
        Deletes a ParameterRoom from the database.

        This method takes a ParameterRooms object, which contains the ID of the ParameterRooms to delete.

        Parameters:
            body (models.ParametersRoomDelete): An object containing the shelter ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted ParametersRoom data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                parameterRoom_deleted = session.query(mysql_models.ParameterRoom).get(body.id)
                session.delete(parameterRoom_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="ParameterRoom successfully deleted",
                data=role_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting ParameterRoom from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_ParameterRoom(self, body: models.ParameterRoomUpdate):
        """
        Updates an existing ParameterRoom in the database.

        This method takes a ParameterRoom object, which contains the updated data for the ParameterRoom,
        and updates the corresponding record in the database.

        Parameters:
            body (models.ParametersRoomUpdate): An object containing the updated ParametersRoom data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated ParameterRoom Role.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                ParameterRoom: mysql_models.ParameterRoom = session.query(mysql_models.ParameterRoom).get(body.id)
                ParameterRoom.id_room = body.id_room
                ParameterRoom.id_parameter = body.id_parameter
                ParameterRoom.iddate = body.date
                ParameterRoom.idvalue = body.value
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="ParameterRoom successfully updated",
                data=ParameterRoom,
                code=201
            )
        except Exception as e:
            print("Error updating ParameterRoom in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
