import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from sqlalchemy.orm import Session
import app.utils.vars as var
from app.mysql.mysql import Nexus1DataBase


class ParameterRoom_Controller:
    """
    Controller for managing ParameterRoom-related operations.

    This class handles the creation, updating, deletion, and retrieval of ParameterRooms in the database.
    """

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the ParameterRoom_Controller class.

        Parameters:
            db (object): An instance of a database (e.g., Nexus1DataBase) that will be used to create the database connection.
        """
        self.db = db  # Recibe la instancia de la base de datos desde fuera
    
    def healthz(self):
        """
        Checks the status of the connection.

        Returns:
            dict: A dictionary with the status "ok".
        """
        return {"status": "ok"}

    def create_parameterRoom(self, body: models.ParameterRoomCreate):
        """
        Creates a new ParameterRoom in the database.

        Parameters:
            body (models.ParameterRoom): An object containing the shelter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.ParameterRoom(id_room=body.id_room, id_parameter=body.id_parameter, date=body.date, value=body.value)
            with Session(self.db.engine) as session:
                session.add(body_row)
                session.commit()
                session.refresh(body_row)
            return ResponseModel(
                status="ok",
                message="ParameterRoom inserted into database successfully",
                data=body_row,
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

        Returns:
            ResponseModel: A response model with the status of the operation, message, and ParameterRoom data.
        """
        try:
            response: list = []
            with Session(self.db.engine) as session:
                response = session.query(mysql_models.ParameterRoom).all()
            return ResponseModel(
                status="ok",
                message="All ParameterRooms successfully retrieved",
                data=response,
                code=200
            )
        except Exception as e:
            print("Error retrieving ParameterRooms from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_parameterRoom(self, body: models.ParameterRoomDelete):
        """
        Deletes a ParameterRoom from the database.

        Parameters:
            body (models.ParameterRoomDelete): An object containing the shelter ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted ParameterRoom data.
        """
        try:
            with Session(self.db.engine) as session:
                parameterRoom_deleted = session.query(mysql_models.ParameterRoom).get(body.id)
                if parameterRoom_deleted:
                    session.delete(parameterRoom_deleted)
                    session.commit()
                    return ResponseModel(
                        status="ok",
                        message="ParameterRoom successfully deleted",
                        data=parameterRoom_deleted,
                        code=200
                    )
                else:
                    return ResponseModel(
                        status="error",
                        message="ParameterRoom not found",
                        data=None,
                        code=404
                    )
        except Exception as e:
            print("Error deleting ParameterRoom from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_parameterRoom(self, body: models.ParameterRoomUpdate):
        """
        Updates an existing ParameterRoom in the database.

        Parameters:
            body (models.ParameterRoomUpdate): An object containing the updated ParameterRoom data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated ParameterRoom data.
        """
        try:
            with Session(self.db.engine) as session:
                parameterRoom: mysql_models.ParameterRoom = session.query(mysql_models.ParameterRoom).get(body.id)
                if parameterRoom:
                    parameterRoom.id_room = body.id_room
                    parameterRoom.id_parameter = body.id_parameter
                    parameterRoom.date = body.date
                    parameterRoom.value = body.value
                    session.commit()
                    return ResponseModel(
                        status="ok",
                        message="ParameterRoom successfully updated",
                        data=parameterRoom,
                        code=200
                    )
                else:
                    return ResponseModel(
                        status="error",
                        message="ParameterRoom not found",
                        data=None,
                        code=404
                    )
        except Exception as e:
            print("Error updating ParameterRoom in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
