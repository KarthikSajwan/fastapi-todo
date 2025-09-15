from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL (SQLite in this case)
#SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:karthik2003@localhost/TodoApplicationDatabase"


# Create engine (for SQLite, need connect_args to avoid threading issues)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Create a session factory
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base class for ORM models
Base = declarative_base()
