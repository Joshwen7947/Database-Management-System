# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create an engine
engine = create_engine('sqlite:///grocery_store.db', echo=True)


# Create all tables
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
def get_session():
    return Session()
