from Model.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Student(Base):
    __tablename__="student"

    registration = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    student_class = Column(String)

    def __repr__(self):
        return f'[Matrícula: {self.registration}\n\
        Nome: {self.name}\n\
        Turma: {self.student_class}'
        