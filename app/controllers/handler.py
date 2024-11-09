import app.models.models as models
from app.models.response_models import ResponseModel
import app.mysql.models as mysql_models
from app.mysql.mysql import Nexus1DataBase

import app.utils.vars as var
from sqlalchemy.orm import Session

class Shelter_Controller:
    def __init__(self) -> None:
        pass
    
    def healhz(self):
        return {"status" : "ok"}
    
    def create_shelter(self, body : models.ShelterCreate):
        try:
            body_row = mysql_models.Shelter(name = body.name,description = body.description)
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                session.add(body_row)
                session.commit()
                session.close()
            return ResponseModel (
                status = "ok",
                message = "Shelter inserted into database succesfull",
                data = None,
                code = 201
            )
        except Exception as e:
            print("Error inserting shelter into database")
            return ResponseModel(
                status = "error",
                message = str(e),
                data = None,
                code = 500
            )


    def get_all(self):
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            response : list = []
            with Session(db.engine) as session:
                response = session.query(mysql_models.Shelter).all()
                session.close()
            return ResponseModel(
                status = "ok",
                message = "All shelter correctly selected",
                data = response,
                code = 201
            )
        except Exception as e:
            print("Error selecting all shelters form database")
            return ResponseModel(
                status = "error",
                message = str(e),
                data = None,
                code = 500
            )

    def delete_shelter(self,body : models.ShelterDelete):
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                shelterDeleted = session.query(mysql_models.Shelter).get(body.id)
                session.delete(shelterDeleted)
                session.commit()
                session.close()
            return ResponseModel (
                status = "ok",
                message = "Shelter correctly deleted",
                data = shelterDeleted,
                code = 201
            ) 
        except Exception as e:
            print("Error deleting shelter from databse")
            return ResponseModel(
                status = "error",
                message = str(e),
                data = None,
                code = 500
            )


    



    def update_shelter(self,body : models.ShelterUpdate):
        try:
            db = Nexus1DataBase(var.MYSQL_URL)
            with Session(db.engine) as session:
                shelter : mysql_models.Shelter = session.query(mysql_models.Shelter).get(body.id)
                shelter.name = body.name
                shelter.description = body.description
                session.dirty 
                session.commit()
                session.close()
                return ResponseModel (
                    status = "ok",
                    message = "Shelter succesfully updated",
                    data = shelter,
                    code = 201
                ) 
        except Exception as e:
            print("Error updating shelter on database")
            return ResponseModel(
                status = "error",
                message = str(e),
                data = None,
                code = 500
            )


