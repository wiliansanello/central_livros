from flask import Flask, render_template, request, redirect, url_for
from routes.books_routes import books_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(books_bp, url_prefix="/books")

    return app
'''@app.route('/')
def index():
    return render_template('index.html')'''



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
