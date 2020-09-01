from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ

# Create sqlalchemy engine
engine = None
env = environ.get('ENV') or 'dev'
if env == 'dev':
    engine = create_engine('sqlite:///db.sqlite3')
else:
    database_url = environ.get('DATABASE_URL')
    engine = create_engine(database_url)

# Create a session
session = sessionmaker(bind=engine)()

# Create base model
Base = declarative_base()
