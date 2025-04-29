from sqlalchemy.orm import joinedload
from sqlalchemy import func
from database.connection import DBConnectionHandler
from Model.entities.book import Book
from Model.entities.author import Author

class BooksRepository:
    def select_all_books(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Book)\
                .options(joinedload(Book.authors))\
                .options(joinedload(Book.genres))\
                .all()
        
        return data
    
    def select_books_by_author(self, author_name):
        with DBConnectionHandler() as db:
            data = db.session.query(Book)\
                .join(Book.authors)\
                .filter(func.lower(Author.name).like(f"%{author_name.lower()}%"))\
                .options(joinedload(Book.authors))\
                .options(joinedload(Book.genres))\
                .all()
        
        return data
    
    def select_books_by_title(self, title):
        with DBConnectionHandler() as db:
            data = db.session.query(Book)\
                .filter(func.lower(Book.title).like(f"%{title.lower()}%"))\
                .options(joinedload(Book.authors))\
                .options(joinedload(Book.genres))\
                .filter_by(Book.title == title)\
                .all()
        
        return data    
    
    def get_or_create_author(self, session, author_name):
        author = session.query(Author).filter_by(name=author_name).first()
        if author:
            return author
        else:
            new_author = Author(name=author_name)
            session.add(new_author)
            session.flush() #garante que o novo autor já tem um id
        return new_author
    

    def insert(self, isbn, title, edition, year, name_authors_list):
        with DBConnectionHandler() as db:
            authors = []
            for name in name_authors_list:
                author = self.get_or_create_author(db.session, name)
                authors.append(author)

            new_book = Book(
                isbn=isbn,
                title=title,
                edition=edition,
                year=year,
                authors=authors
            )

            db.session.add(new_book)
            db.session.commit()
            db.session.refresh(new_book)

        return new_book
    
    def update(self, isbn, new_title=None, new_edition=None, new_year=None):
        with DBConnectionHandler() as db:
            book = db.session.query(Book).filter(Book.isbn == isbn).first()
            if not book:
                return None
        
        if new_title: 
            book.title = new_title
        if new_edition:
            book.edition = new_edition
        if new_year:
            book.year = new_year

        db.session.commit()
        return book
        
    def delete(self, isbn):
        with DBConnectionHandler() as db:
            book = db.session.query(Book).filter(isbn == isbn).first()
            if not book:
                return False
            
            db.session.delete(book)
            db.session.commit()
            return True