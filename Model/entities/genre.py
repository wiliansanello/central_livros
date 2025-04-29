from Model.base import Base
from Model.entities.book_genre_relationship import books_has_genres
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Genre(Base):

    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

    books = relationship(
        'Book',
        secondary=books_has_genres,
        back_populates='genres'

    )