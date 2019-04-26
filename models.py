import os
import dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

db = os.getenv('DATABASE')

db_connection = "{}:{}@{}:{}/{}".format(
    os.getenv('DB_USER'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_DB')
)

engine = create_engine("mysql+mysqldb://{}".format(db_connection), echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
