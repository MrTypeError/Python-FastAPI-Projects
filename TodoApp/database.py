from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Sanu@2025!@localhost/TodoApplication'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Sanu%402025%21@localhost/TodoApplication'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()