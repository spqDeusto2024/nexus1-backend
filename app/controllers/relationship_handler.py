import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session


class Relationship_Controller:
    """
    Controller for managing relationship-related operations.

    This class handles the creation, updating, deletion, and retrieval of relationships in the database.

    
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Relationship_Controller class.

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

    def create_relationship(self, body: models.RelationshipCreate):
        """
        Creates a new relationship in the database.

        This method takes a RelationshipCreate object, which contains the necessary data to create a relationship
        and saves it to the database.

        Parameters:
            body (models.RelationshipCreate): An object containing the relationship data to create.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and response data.
        """
        try:
            body_row = mysql_models.Relationship(
                name=body.name,
                description=body.description
            )
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Relationship inserted into database successfully",
                data=None,
                code=201
            )
        except Exception as e:
            print("Error inserting relationship into database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def get_all(self):
        """
        Retrieves all relationships from the database.

        This method queries all relationship records in the database and returns them.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and relationship data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response: list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.Relationship).all()
                session.close()
            return ResponseModel(
                status="ok",
                message="All relationships successfully retrieved",
                data=response,
                code=201
            )
        except Exception as e:
            print("Error retrieving relationships from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def delete_relationship(self, body: models.RelationshipDelete):
        """
        Deletes a relationship from the database.

        This method takes a RelationshipDelete object, which contains the ID of the relationship to delete.

        Parameters:
            body (models.RelationshipDelete): An object containing the relationship ID to delete.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and deleted relationship data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                relationship_deleted = session.query(mysql_models.Relationship).get(body.id)
                session.delete(relationship_deleted)
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Relationship successfully deleted",
                data=relationship_deleted,
                code=201
            )
        except Exception as e:
            print("Error deleting relationship from database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

    def update_relationship(self, body: models.RelationshipUpdate):
        """
        Updates an existing relationship in the database.

        This method takes a RelationshipUpdate object, which contains the updated data for the relationship,
        and updates the corresponding record in the database.

        Parameters:
            body (models.RelationshipUpdate): An object containing the updated relationship data.

        Returns:
            ResponseModel: A response model with the status of the operation, message, and updated relationship data.
        """
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                relationship: mysql_models.Relationship = session.query(mysql_models.Relationship).get(body.id)
                relationship.name=body.name
                relationship.description=body.description
                
                session.dirty  # This seems redundant; the session will be dirty when an attribute is modified
                session.commit()
                session.close()
            return ResponseModel(
                status="ok",
                message="Relationship successfully updated",
                data=relationship,
                code=201
            )
        except Exception as e:
            print("Error updating relationship in database")
            return ResponseModel(
                status="error",
                message=str(e),
                data=None,
                code=500
            )

