CREATE TABLE book (
    isbn    INTEGER PRIMARY KEY NOT NULL,
    title   TEXT    NOT NULL,
    edition INTEGER,
    year    INTEGER
);
            
CREATE TABLE author (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    NOT NULL
);
            
CREATE TABLE books_has_authors (
    book_isbn INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (
        book_isbn
    )
    REFERENCES book (isbn),
    FOREIGN KEY (
        author_id
    )
    REFERENCES author (id) 
);


CREATE TABLE genre (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT    NOT NULL
);

CREATE TABLE books_has_genres (
    book_isbn INTEGER NOT NULL,
    genre_id  INTEGER NOT NULL,
    PRIMARY KEY (
        book_isbn,
        genre_id
    ),
    FOREIGN KEY (
        book_isbn
    )
    REFERENCES book (isbn),
    FOREIGN KEY (
        genre_id
    )
    REFERENCES genre (id) 
);


CREATE TABLE student (
    registration  INTEGER NOT NULL,
    name          TEXT    NOT NULL,
    student_class TEXT
);
            
CREATE TABLE contact (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    type    TEXT    NOT NULL,
    contact TEXT    NOT NULL
);

CREATE TABLE students_has_contacts (
    student_registration INTEGER NOT NULL,
    contact_id           INTEGER NOT NULL,
    PRIMARY KEY (
        student_registration,
        contact_id
    ),
    FOREIGN KEY (
        student_registration
    )
    REFERENCES student (registration),
    FOREIGN KEY (
        contact_id
    )
    REFERENCES contact (id) 
);

CREATE TABLE loan (
    id           INTEGER      PRIMARY KEY AUTOINCREMENT,
    registration INTEGER      NOT NULL,
    isbn         INTEGER      NOT NULL,
    date         DATETIME     NOT NULL,
    days_late    INT,
    value_fine   FLOAT (3, 2),
    FOREIGN KEY (
        registration
    )
    REFERENCES student (registration),
    FOREIGN KEY (
        isbn
    )
    REFERENCES book (isbn) 
);
