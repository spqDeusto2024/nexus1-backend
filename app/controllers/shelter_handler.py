import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
# from app.mysql.mysql import Nexus1DataBase, TestDataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class Shelter_Controller:
    """
    Controller for managing shelter-related operations.

    This class handles the creation, updating, deletion, and retrieval of shelters in the database.
    """

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the Shelter_Controller class.

        Parameters:
            db (object): An instance of a database (e.g., Nexus1DataBase or TestDataBase) that will be used to create the database connection.
        """
        self.db = db  # Ya se pasa directamente la instancia de la base de datos

    def healthz(self):
        """
        Checks the status of the connection.

        Returns:
            dict: A dictionary with the status "ok".
        """
        return {"status": "ok"}

    def create_shelter(self, body: models.ShelterCreate):
        """
        Creates a new shelter in the database.

        Parameters:
            body (models.ShelterCreate): An object containing the shelter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Shelter(name=body.name, description=body.description)
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                session.add(body_row)
                session.commit()
                session.refresh(body_row)
                session.close()
            return ResponseModel(
                status="ok",
                message="Shelter inserted into database successfully",
                data=body_row,
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

        Returns:
            ResponseModel: A response model with the status of the operation, message, and shelter data.
        """
        try:
            response: list = []
            with Session(self.db.engine) as session:  # Usamos self.db directamente
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

        Parameters:
            body (models.ShelterDelete): An object containing the shelter ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted shelter data.
        """
        try:
            with Session(self.db.engine) as session:  # Usamos self.db directamente
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

        Parameters:
            body (models.ShelterUpdate): An object containing the updated shelter data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated shelter data.
        """
        try:
            with Session(self.db.engine) as session:  # Usamos self.db directamente
                shelter: mysql_models.Shelter = session.query(mysql_models.Shelter).get(body.id)
                shelter.name = body.name
                shelter.description = body.description
                session.dirty  # La sesión se marca como sucia automáticamente
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
