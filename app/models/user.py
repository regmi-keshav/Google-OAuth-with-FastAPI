from sqlalchemy import Column, String
from db.database import Base


class User(Base):
    __tablename__ = "auth"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    extend_existing = True  # This line allows redefining the table
