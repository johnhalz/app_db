from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, Boolean, ForeignKey, UUID
from sqlalchemy.orm import relationship

from .bases import ProductionBase
from .user_preference import UserPreference

class UserRole(Enum):
    admin = 'Admin'
    system_engineer = 'System Engineer'
    test_engineer = 'Test Engineer'
    data_scientist = 'Data Scientist'
    test_operator = 'Test Operator'
    mechanic = 'Mechanic'

class User(ProductionBase):
    __tablename__ = 'user_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(150), nullable=False)
    encrypted_pw = Column(String(256), nullable=False)
    role = Column(String(50), nullable=False)
    external = Column(Boolean, nullable=False)

    comment = relationship('Comment', back_populates='user')
    non_compliance_reporter = relationship('NonCompliance', back_populates='user')
    non_compliance_signer = relationship('NonCompliance', back_populates='user')
    production_step_oprator = relationship('ProductionStep', back_populates='user')

    user_preference_id = Column(UUID(as_uuid=True), ForeignKey('user_preference_table.id'))
    user_preference = relationship('UserPreference', back_populates='user')

    def __init__(self, first_name: str, last_name: str, encrpyted_password: str,
                 user_preference: UserPreference, role: str, id: UUID = uuid4(), username: str = None, external: bool = False):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.encrypted_pw = encrpyted_password
        self.role = role
        self.external = external
        self.username = self.__define_username(username)
        self.user_preference_id = user_preference.id

    def __define_username(self, username: str = None) -> str:
        if username is None:
            if self.first_name is None or self.last_name is None:
                raise ValueError(
                    'First and last names must be set in order to define a username!'
                )

            username = f'{self.first_name}.{self.last_name}'.lower()

            if self.external:
                username = 'extern.' + username

            return username

        return username
