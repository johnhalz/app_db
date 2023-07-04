from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID
from sqlalchemy.ext.declarative import declarative_base

UserBase = declarative_base()

class UserRole(Enum):
    admin = 'Admin'
    system_engineer = 'System Engineer'
    test_engineer = 'Test Engineer'
    data_scientist = 'Data Scientist'
    test_operator = 'Test Operator'
    mechanic = 'Mechanic'


class User(UserBase):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(150), nullable=False)
    encrypted_pw = Column(String(256), nullable=False)
    user_preference_id = Column(UUID(as_uuid=True), nullable=False)
    role = Column(String(50), nullable=False)

    def __init__(self, first_name: str, last_name: str, encrpyted_password: str,
                 user_preference_id: UUID, role: str, id: UUID = uuid4(), username: str = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.encrypted_pw = encrpyted_password
        self.user_preference_id = user_preference_id
        self.role = role
        self.username = self.__define_username(username)

    def __define_username(self, username: str = None) -> str:
        if username is None:
            if self.first_name is None or self.last_name is None:
                raise ValueError(
                    'First and last names must be set in order to define a username!'
                )

            return f'{self.first_name}.{self.last_name}'.lower()

        return username
