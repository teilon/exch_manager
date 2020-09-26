import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

POSTGRES_HOST = os.environ['POSTGRES_HOST'] #'78.155.206.12'
POSTGRES_PORT = os.environ['POSTGRES_PORT'] #'5432'
POSTGRES_DATABASE = os.environ['POSTGRES_DB'] #'postgres_db'
POSTGRES_USER = os.environ['POSTGRES_USER'] #'torn'
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD'] #'helicopter'

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.\
    format(POSTGRES_USER,
           POSTGRES_PASSWORD,
           POSTGRES_HOST,
           POSTGRES_PORT,
           POSTGRES_DATABASE)
