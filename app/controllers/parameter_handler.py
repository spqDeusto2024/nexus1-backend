import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class Parameter_Controller:
    """
    Controller for managing Parameter-related operations.

    This class handles the creation, updating, deletion, and retrieval of Parameters in the database.

    
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Parameter_Controller class.

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

    def create_parameter(self, body: models.ParameterCreate):
        """
        Creates a new Parameter in the database.

        This method takes a Parameter object, which contains the necessary data to create a Parameter
        and saves it to the database.

        Parameters:
            body (models.Parameter): An object containing the shelter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Parameter(name = body.name, description= body.description)
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Parameter inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting Parameter into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all Parameters from the database.

        This method queries all Parameters records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and Parameter data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.Parameter).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All Parameters successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving Parameters from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_parameter(self, body: models.ParameterDelete):
        """
        Deletes a Parameter from the database.

        This method takes a Parameters object, which contains the ID of the Parameters to delete.

        Parameters:
            body (models.ParametersDelete): An object containing the shelter ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted Parameters data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                parameter_deleted = session.query(mysql_models.Parameter).get(body.id)
                session.delete(parameter_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Parameter successfully deleted",
                data=parameter_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting Parameter from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_parameter(self, body: models.ParameterUpdate):
        """
        Updates an existing Parameter in the database.

        This method takes a Parameter object, which contains the updated data for the Parameter,
        and updates the corresponding record in the database.

        Parameters:
            body (models.ParametersUpdate): An object containing the updated Parameters data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated Parameter.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                Parameter: mysql_models.Parameter = session.query(mysql_models.Parameter).get(body.id)
                Parameter.name = body.name
                Parameter.description = body.description
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Parameter successfully updated",
                data=Parameter,
                code=201
            )
        except Exception as e:
            print("Error updating Parameter in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
