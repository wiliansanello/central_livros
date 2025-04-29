from flask import Blueprint, jsonify, request
from Model.repositories.books_repository import BooksRepository

books_bp = Blueprint("books",__name__)
repo = BooksRepository()

@books_bp.route("/", methods=["GET"])
def list_books():
    books = repo.select_all_books()
    books_data = []
    for book in books:
        books_data.append({
            "id": book.isbn,
            "isbn": book.isbn,
            "title": book.title,
            "edition": book.edition,
            "year": book.year,
            "authors": [author.name for author in book.authors],
            "genres": [genre.description for genre in book.genres]
        })
    return jsonify(books_data)

@books_bp.route("/author/<author_name>", methods=["GET"])
def get_books_by_author(author_name):
    books = repo.select_books_by_author(author_name)
    books_data = []
    for book in books:
        books_data.append({
            "id": book.isbn,
            "isbn": book.isbn,
            "title": book.title,
            "edition": book.edition,
            "year": book.year,
            "authors": [author.name for author in book.authors],
            "genres": [genre.description for genre in book.genres]
        })    
    return jsonify(books_data)

@books_bp.route("/title/<title>", methods=["GET"])
def get_books_by_title(title):
    books = repo.select_books_by_title(title)
    books_data = []
    for book in books:
        books_data.append({
            "id": book.isbn,
            "isbn": book.isbn,
            "title": book.title,
            "edition": book.edition,
            "year": book.year,
            "authors": [author.name for author in book.authors],
            "genres": [genre.description for genre in book.genres],
        })
    return jsonify(books_data)

@books_bp.route("/", methods=["POST"])
def create_book():
    data = request.get_json()

    isbn = data.get("isbn")
    title = data.get("title")
    edition = data.get("edition")
    year = data.get("year")
    authors = data.get("authors", [])

    if not (isbn and title and edition and year and authors):
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400
    
    book = repo.insert(isbn, title, edition, year, authors)

    return jsonify({
        "id": book.isbn,
        "title": book.title
    }), 201

@books_bp.route("/<int:isbn>", methods=["PUT"])
def update_book(isbn):
    data = request.get_json()

    new_title = data.get("title")
    new_edition = data.get("edition")
    new_year = data.get("year")

    book = repo.update(isbn, new_title, new_edition, new_year)

    if not book:
        return jsonify({"error":"Livro não encontrado"}), 404
    
    return jsonify({
        "message": "Livro atualizado com sucesso",
        "isbn": book.isbn
    })

@books_bp.route("/<int:book_isbn>", methods=["DELETE"])
def delete(book_isbn):
    result = repo.delete(book_isbn)

    if not result:
        return jsonify({"error": "Livro não encontrado"}), 404

    return jsonify ({"message": "Livro excluído com sucesso"})