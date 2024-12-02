import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from sqlalchemy.orm import Session

class Room_Controller:
    """
    Controller for managing Room-related operations.

    This class handles the creation, updating, deletion, and retrieval of rooms in the database.
    """

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the Room_Controller class.

        Parameters:
            db (object): An instance of a database (e.g., Nexus1DataBase) that will be used to create the database connection.
        """
        self.db = db  # Recibe la instancia de la base de datos desde fuera

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
            body (models.RoomCreate): An object containing the room data to create.

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
            with Session(self.db.engine) as session:
                session.add(body_row)
                session.commit()
                session.refresh(body_row)
                session.close()
            return ResponseModel(
                status="ok",
                message="Room inserted into database successfully",
                data=body_row,
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

        This method queries all room records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and rooms data.
        """
        try:
            with Session(self.db.engine) as session:
                response = session.query(mysql_models.Room).all()
            return ResponseModel(
                status="ok",
                message="All rooms successfully retrieved",
                data=response,
                code=200
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
            with Session(self.db.engine) as session:
                room_deleted = session.query(mysql_models.Room).get(body.id)
                if room_deleted:
                    session.delete(room_deleted)
                    session.commit()
                else:
                    raise Exception("Room not found")
            return ResponseModel(
                status="ok",
                message="Room successfully deleted",
                data=room_deleted,
                code=200
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
        Updates an existing room in the database.

        This method takes a RoomUpdate object, which contains the updated data for the room,
        and updates the corresponding record in the database.

        Parameters:
            body (models.RoomUpdate): An object containing the updated room data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated room data.
        """
        try:
            with Session(self.db.engine) as session:
                room = session.query(mysql_models.Room).get(body.id)
                if room:
                    room.name = body.name
                    room.description = body.description
                    room.capacity = body.capacity
                    room.actual_tenant_number = body.actual_tenant_number
                    room.availability = body.availability
                    session.commit()
                    session.refresh(room)   
                else:
                    raise Exception("Room not found")
            return ResponseModel(
                status="ok",
                message="Room successfully updated",
                data=room,
                code=200
            )
        except Exception as e:
            print("Error updating room in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
