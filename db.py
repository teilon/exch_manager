from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

POSTGRES_HOST = '78.155.206.12'
POSTGRES_PORT = '5432'
POSTGRES_DATABASE = 'postgres_db'
POSTGRES_USER = 'torn'
POSTGRES_PASSWORD = 'helicopter'

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.\
    format(POSTGRES_USER,
           POSTGRES_PASSWORD,
           POSTGRES_HOST,
           POSTGRES_PORT,
           POSTGRES_DATABASE)