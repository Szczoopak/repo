from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import os

DATABASE_URL = os.getenv("DATABASE_URL")
db_engine = create_engine(DATABASE_URL)
# DATABASE_URL = "sqlite:///./indoor_system.db"
DATABASE_URL = "postgresql://postgres:haslo@localhost:5432/indoor_system"
DBSession = sessionmaker(
    bind=db_engine, 
    autocommit=False, 
    autoflush=False
)
ORMBaseModel = declarative_base()

def get_db_session():
    db_session = DBSession()
    try:
        yield db_session 
    finally:
        db_session.close()
