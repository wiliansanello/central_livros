from Model.repositories.books_repository import BooksRepository
from seed_data import seed_data
from database.connection import DBConnectionHandler
from Model.entities.book import Book

def initialize_database():
    with DBConnectionHandler() as db:
        books_count = db.session.query(Book).count()
        if books_count == 0:
            print("Nenhum dado encontrado no banco. Populando a base de dados...")
            seed_data()
        else:
            print(f"Banco de dados já possui {books_count} livros. Pulando seed...")

def main():
    initialize_database()

    repo = BooksRepository()
    response = repo.select_all_books()

    print("\n=== LIVROS CADASTRADOS ===\n")
    for book in response:
        print(book)
        print("-"*50)
    
if __name__ == "__main__":
    main()