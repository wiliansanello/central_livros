from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from utils.db import init_db, get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livros')
def listar_livros():
    conn = get_db_connection()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()
    return render_template('listar_livros.html', livros=livros)

@app.route('/livros/cadastrar', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = request.form['ano']
        conn = get_db_connection()
        conn.execute('INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)', (titulo, autor, ano))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_livros'))
    return render_template('cadastrar_livro.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
