from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Create the database engine
engine = create_engine(settings.DATABASE_URL, echo=True)

# Create a sessionmaker for synchronous sessions
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# Create a base class for our models
Base = declarative_base()

# Function to initialize the database schema


def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency to get the database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
