from Model.base import Base
from Model.entities.book_author_relationship import books_has_authors
from Model.entities.book_genre_relationship import books_has_genres
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "book"

    isbn = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    edition = Column(Integer)
    year = Column(Integer)

    authors = relationship('Author', 
                         secondary=books_has_authors,
                         back_populates='books')
    
    genres = relationship('Genre',
                          secondary=books_has_genres,
                          back_populates='books')

    def __repr__(self):
        authors = ','.join(author.name for author in self.authors)
        genres = ','.join(genre.description for genre in self.genres)
        return f"[ISBN: {self.isbn}\n\
        Título: {self.title}\n\
        Autor: {authors}\n\
        Edição: {self.edition}\n\
        Ano: {self.year}\n\
        Gênero: {genres}]\n\n"
    
    