import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class Room_Controller:
    """
    Controller for managing Room-related operations.

    This class handles the creation, updating, deletion, and retrieval of rooms in the database.

   
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Room_Controller class.

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

    def create_room(self, body: models.RoomCreate):
        """
        Creates a new room in the database.

        This method takes a RoomCreate object, which contains the necessary data to create a room
        and saves it to the database.

        Parameters:
            body (models.RoomCreate): An object containing the shelter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Room(
                id_shelter=body.id_shelter,
                name=body.name,
                description=body.description,
                capacity=body.capacity,
                actual_tenant_number=body.actual_tenant_number,
                availability=body.availability)
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Room inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting Room into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )


    def get_all(self):
            """
            Retrieves all rooms from the database.

            This method queries all rooms records in the database and returns them.

            Returns:
                ResponseModel: A response model with the status of the operation, message, and rooms data.
            """
            try:
                db = Nexus1DataBase(var.MYSQL_URL)
                response: list = []
                with Session(db.engine) as session:
                    response = session.query(mysql_models.Room).all()
                    session.close()
                return ResponseModel(
                    status="ok",
                    message="All rooms successfully retrieved",
                    data=response,
                    code=201
                )
            except Exception as e:
                print("Error retrieving rooms from database")
                return ResponseModel(
                    status="error",
                    message=str(e),
                    data=None,
                    code=500
                )

    def delete_room(self, body: models.RoomDelete):
            """
            Deletes a room from the database.

            This method takes a RoomDelete object, which contains the ID of the room to delete.

            Parameters:
                body (models.RoomDelete): An object containing the room ID to delete.

            Returns:
                ResponseModel: A response model with the status of the operation, message, and deleted room data.
            """
            try:
                db = Nexus1DataBase(var.MYSQL_URL)
                with Session(db.engine) as session:
                    room_deleted = session.query(mysql_models.Room).get(body.id)
                    session.delete(room_deleted)
                    session.commit()
                    session.close()
                return ResponseModel(
                    status="ok",
                    message="Room successfully deleted",
                    data=room_deleted,
                    code=201
                )
            except Exception as e:
                print("Error deleting room from database")
                return ResponseModel(
                    status="error",
                    message=str(e),
                    data=None,
                    code=500
                ) 
    
    def update_room(self, body: models.RoomUpdate):
        """
        Updates an existing dormitory in the database.

        This method takes a DormitoryUpdate object, which contains the updated data for the dormitory,
        and updates the corresponding record in the database.

        Parameters:
            body (models.DormitoryUpdate): An object containing the updated dormitory data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated dormitory data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                room: mysql_models.Room = session.query(mysql_models.Room).get(body.id)
                room.name = body.name
                room.description = body.description
                room.capacity = body.capacity
                room.actual_tenant_number = body.actual_tenant_number
                room.availability = body.availability
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Room successfully updated",
                data=room,
                code=201
            )
        except Exception as e:
            print("Error updating room in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )