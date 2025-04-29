from Model.base import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

books_has_genres = Table(
    'books_has_genres',
    Base.metadata,
    Column('book_isbn', Integer, ForeignKey('book.isbn'),primary_key=True),
    Column('genre_id', Integer, ForeignKey('genre.id'), primary_key=True)
)