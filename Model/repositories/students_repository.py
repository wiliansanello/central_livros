from sqlalchemy.orm import joinedload
from sqlalchemy import func
from database.connection import DBConnectionHandler
from Model.entities.student import Student
from Model.entities.contact import Contact

class StudentsRepository:
    def select_all_students(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Student)\
            .all()

        return data
