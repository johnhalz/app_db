from uuid import uuid4
from sqlalchemy import Column, String, UUID
from sqlalchemy.ext.declarative import declarative_base

UserBase = declarative_base()

class User(UserBase):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True, default=uuid4())
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(150), nullable=False)
    encrypted_pw = Column(String(50), nullable=False)
    user_preference_id = Column(UUID, nullable=False)
    role = Column(String(50), nullable=False)
