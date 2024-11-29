import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from sqlalchemy.orm import Session


class Dormitory_Controller:
    """
    Controller for managing dormitory-related operations.

    This class handles the creation, updating, deletion, and retrieval of dormitories in the database.
    """

    def __init__(self, db: object) -> None:
        """
        Initializes a new instance of the Dormitory_Controller class.

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

    def create_dormitory(self, body: models.DormitoryCreate):
        """
        Creates a new dormitory in the database.

        This method takes a DormitoryCreate object, which contains the necessary data to create a dormitory
        and saves it to the database.

        Parameters:
            body (models.DormitoryCreate): An object containing the dormitory data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Dormitory(
                id_shelter=body.id_shelter,
                name=body.name,
                description=body.description,
                capacity=body.capacity,
                actual_tenant_number=body.actual_tenant_number,
                availability=body.availability
            )
            with Session(self.db.engine) as session:
                session.add(body_row)
                session.commit()
                session.refresh(body_row)
                session.close()
            return ResponseModel(
                status="ok",
                message="Dormitory inserted into database successfully",
                data=body_row,
                code=201
            )
        except Exception as e:
            return ResponseModel(
                status="error",
                message=f"Error inserting dormitory into database: {str(e)}",
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all dormitories from the database.

        This method queries all dormitory records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and dormitory data.
        """
        try:
            with Session(self.db.engine) as session:
                response = session.query(mysql_models.Dormitory).all()
            return ResponseModel(
                status="ok",
                message="All dormitories successfully retrieved",
                data=response,
                code=200
            )
        except Exception as e:
            return ResponseModel(
                status="error",
                message=f"Error retrieving dormitories from database: {str(e)}",
                data=None,
                code=500
            )

    def delete_dormitory(self, body: models.DormitoryDelete):
        """
        Deletes a dormitory from the database.

        This method takes a DormitoryDelete object, which contains the ID of the dormitory to delete.

        Parameters:
            body (models.DormitoryDelete): An object containing the dormitory ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted dormitory data.
        """
        try:
            with Session(self.db.engine) as session:
                dormitory_deleted = session.query(mysql_models.Dormitory).get(body.id)
                if dormitory_deleted:
                    session.delete(dormitory_deleted)
                    session.commit()
                    session.close()
                else:
                    raise Exception("Dormitory not found")
            return ResponseModel(
                status="ok",
                message="Dormitory successfully deleted",
                data=dormitory_deleted,
                code=200
            )
        except Exception as e:
            return ResponseModel(
                status="error",
                message=f"Error deleting dormitory from database: {str(e)}",
                data=None,
                code=500
            )

    def update_dormitory(self, body: models.DormitoryUpdate):
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
            with Session(self.db.engine) as session:
                dormitory = session.query(mysql_models.Dormitory).get(body.id)
                if dormitory:
                    dormitory.name = body.name
                    dormitory.description = body.description
                    dormitory.capacity = body.capacity
                    dormitory.actual_tenant_number = body.actual_tenant_number
                    dormitory.availability = body.availability
                    session.commit()
                    session.close()
                else:
                    raise Exception("Dormitory not found")
            return ResponseModel(
                status="ok",
                message="Dormitory successfully updated",
                data=dormitory,
                code=200
            )
        except Exception as e:
            return ResponseModel(
                status="error",
                message=f"Error updating dormitory in database: {str(e)}",
                data=None,
                code=500
            )
