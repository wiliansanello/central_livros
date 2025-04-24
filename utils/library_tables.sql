            CREATE TABLE livro (
                isbn INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                edicao INTEGER,
                ano INTEGER
            )
                     
            CREATE TABLE autor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL                
            )
                     
            CREATE TABLE livro_autor (
                livro_isbn INTEGER NOT NULL,
                autor_iid INTEGER NOT NULL,
                FOREIGN KEY livro_isbn REFERENCES livro(livro.isbn) ON UPDATE CASCADE,
                FOREIGN KEY autor.id REFERENCES autor(autor.id) ON UPDATE CASCADE
            )

            CREATE TABLE genero (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
            )

            CREATE TABLE livro_genero (
                FOREIGN KEY livro.id REFERENCES livro(id),
                FOREIGN KEY genero.id REFERENCES genero(id) 
            )
            
            CREATE TABLE aluno (
                matricula INTEGER NOT NULL,
                nome TEXT NOT NULL,
                turma TEXT
            )
                     
            CREATE TABLE contato (
                id_contato INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                contato TEXT NOT NULL
            )

            CREATE TABLE EMPRESTIMO (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno.matricula INTEGER NOT NULL,
                livro.isbn INTEGER NOT NULL,
                data DATETIME NOT NULL,
                dias_atraso INT,
                valor_multa FLOAT(3,2),
                FOREIGN KEY (aluno.matricula) REFERENCES aluno(matricula),
                FOREIGN KEY (livro.isbn) REFERENCES livro(isbn)
            )
                     
            
