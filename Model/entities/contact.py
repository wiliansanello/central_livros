from Model.base import Base
from sqlalchemy import Column, Integer, String

class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key = True, nullable = False)
    contact_type = Column(String, nullable = False)
    description = Column(String, nullable = False)