from Model.base import Base
from Model.entities.book_author_relationship import books_has_authors
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship

class Author(Base): 
    __tablename__="author"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) 

    books = relationship('Book',
                         secondary=books_has_authors,
                         back_populates='authors')