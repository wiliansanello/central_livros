from Model.base import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

books_has_authors = Table(
    'books_has_authors',
    Base.metadata,
    Column('book_isbn', Integer, ForeignKey('book.isbn'),primary_key=True),
    Column('author_id', Integer, ForeignKey('author.id'),primary_key=True)
)