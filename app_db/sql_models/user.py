from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, Boolean, ForeignKey, UUID
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class UserRole(Enum):
    ADMIN = 'Admin'
    SYSTEM_ENGINEER = 'System Engineer'
    TEST_ENGINEER = 'Test Engineer'
    DATA_SCIENTIST = 'Data Scientist'
    TEST_OPERATOR = 'Test Operator'
    MECHANIC = 'Mechanic'

class User(ProductionBase):
    __tablename__ = 'user_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    external = Column(Boolean, nullable=False, default=False)
    username = Column(String(150), nullable=False, default='')
    encrypted_pw = Column(String(256), nullable=False)
    role_string = Column(String(50), nullable=False)
    user_preference_id = Column(UUID(as_uuid=True), ForeignKey('user_preference_table.id'))

    user_preference = relationship('UserPreference', foreign_keys=[user_preference_id])

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if self.username == '':
            self.username = self.__default_username()

    def __default_username(self) -> str:
        return f'{self.first_name}.{self.last_name}'.lower()

    @property
    def role(self) -> UserRole:
        return UserRole(self.role_string)
