import random
from database.connection import DBConnectionHandler
from Model.entities.author import Author
from Model.entities.genre import Genre
from Model.entities.book import Book

def seed_data():
    with DBConnectionHandler() as db:
        # Criar autores
        authors = [
            Author(name="Machado de Assis"),
            Author(name="Clarice Lispector"),
            Author(name="Graciliano Ramos"),
            Author(name="Jorge Amado"),
            Author(name="Cecília Meireles")
        ]

        # Criar gêneros
        genres = [
            Genre(description="Romance"),
            Genre(description="Ficção"),
            Genre(description="Poesia"),
            Genre(description="Drama"),
            Genre(description="Conto")
        ]

        db.session.add_all(authors + genres)
        db.session.commit()  # Commit pra garantir IDs gerados

        # Criar livros
        books = []
        for i in range(1, 11):  # 10 livros
            book = Book(
                isbn=i,
                title=f"Livro {i}",
                edition=random.randint(1, 5),
                year=random.randint(1880, 2024),
                authors=random.sample(authors, k=random.randint(1, 2)),  # 1 ou 2 autores
                genres=random.sample(genres, k=random.randint(1, 2))     # 1 ou 2 gêneros
            )
            books.append(book)

        db.session.add_all(books)
        db.session.commit()

        print(f"{len(authors)} autores, {len(genres)} gêneros e {len(books)} livros inseridos com sucesso!")

if __name__ == "__main__":
    seed_data()
