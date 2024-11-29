import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from sqlalchemy.orm import Session

import app.utils.vars as var


class Parameter_Controller:
    """
    Controller for managing Parameter-related operations.

    This class handles the creation, updating, deletion, and retrieval of Parameters in the database.
    """

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the Parameter_Controller class.

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

    def create_parameter(self, body: models.ParameterCreate):
        """
        Creates a new Parameter in the database.

        This method takes a Parameter object, which contains the necessary data to create a Parameter
        and saves it to the database.

        Parameters:
            body (models.ParameterCreate): An object containing the parameter data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Parameter(name=body.name, description=body.description)
            with Session(self.db.engine) as session:
                session.add(body_row)
                session.commit()
                session.refresh(body_row)
            return ResponseModel(
                status="ok",
                message="Parameter inserted into database successfully",
                data=body_row,
                code=201
            )
        except Exception as e:
            print(f"Error inserting Parameter into database: {e}")
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
            ResponseModel: A response model with the status of the operation, message, and parameter data.
        """
        try:
            response: list = []
            with Session(self.db.engine) as session:
                response = session.query(mysql_models.Parameter).all()
            return ResponseModel(
                status="ok",
                message="All Parameters successfully retrieved",
                data=response,
                code=200
            )
        except Exception as e:
            print(f"Error retrieving Parameters from database: {e}")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_parameter(self, body: models.ParameterDelete):
        """
        Deletes a Parameter from the database.

        This method takes a Parameter object, which contains the ID of the Parameter to delete.

        Parameters:
            body (models.ParameterDelete): An object containing the parameter ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted parameter data.
        """
        try:
            with Session(self.db.engine) as session:
                parameter_deleted = session.query(mysql_models.Parameter).get(body.id)
                if parameter_deleted:
                    session.delete(parameter_deleted)
                    session.commit()
                    return ResponseModel(
                        status="ok",
                        message="Parameter successfully deleted",
                        data=parameter_deleted,
                        code=200
                    )
                else:
                    return ResponseModel(
                        status="error",
                        message="Parameter not found",
                        data=None,
                        code=404
                    )
        except Exception as e:
            print(f"Error deleting Parameter from database: {e}")
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
            body (models.ParameterUpdate): An object containing the updated parameter data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated parameter.
        """
        try:
            with Session(self.db.engine) as session:
                parameter: mysql_models.Parameter = session.query(mysql_models.Parameter).get(body.id)
                if parameter:
                    parameter.name = body.name
                    parameter.description = body.description
                    session.commit()
                    return ResponseModel(
                        status="ok",
                        message="Parameter successfully updated",
                        data=parameter,
                        code=200
                    )
                else:
                    return ResponseModel(
                        status="error",
                        message="Parameter not found",
                        data=None,
                        code=404
                    )
        except Exception as e:
            print(f"Error updating Parameter in database: {e}")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )
