from Model import Base
from database.connection import DBConnectionHandler

def create_db():
    db_handler = DBConnectionHandler()
    engine = db_handler.engine
    Base.metadata.create_all(engine)

if __name__ == "main":
    create_db()