import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class Shelter_Controller:
    """
    Controller for managing shelter-related operations.

    This class handles the creation, updating, deletion, and retrieval of shelters in the database.

  
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Shelter_Controller class.

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

    def create_shelter(self, body: models.ShelterCreate):
        """
        Creates a new shelter in the database.

        This method takes a ShelterCreate object, which contains the necessary data to create a shelter
        and saves it to the database.

        Parameters:
            body (models.ShelterCreate): An object containing the shelter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Shelter(name=body.name, description=body.description)
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Shelter inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting shelter into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all shelters from the database.

        This method queries all shelter records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and shelter data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.Shelter).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All shelters successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving shelters from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_shelter(self, body: models.ShelterDelete):
        """
        Deletes a shelter from the database.

        This method takes a ShelterDelete object, which contains the ID of the shelter to delete.

        Parameters:
            body (models.ShelterDelete): An object containing the shelter ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted shelter data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                shelter_deleted = session.query(mysql_models.Shelter).get(body.id)
                session.delete(shelter_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Shelter successfully deleted",
                data=shelter_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting shelter from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_shelter(self, body: models.ShelterUpdate):
        """
        Updates an existing shelter in the database.

        This method takes a ShelterUpdate object, which contains the updated data for the shelter,
        and updates the corresponding record in the database.

        Parameters:
            body (models.ShelterUpdate): An object containing the updated shelter data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated shelter data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                shelter: mysql_models.Shelter = session.query(mysql_models.Shelter).get(body.id)
                shelter.name = body.name
                shelter.description = body.description
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Shelter successfully updated",
                data=shelter,
                code=201
            )
        except Exception as e:
            print("Error updating shelter in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
