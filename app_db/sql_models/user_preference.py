from uuid import uuid4, UUID
from enum import Enum

from sqlalchemy import Column, String, Boolean, Integer, UUID
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class UserPreference(ProductionBase):
    __tablename__ = 'user_preference_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    app_lighting = Column(String(10), nullable=False)
    language = Column(String(10), nullable=False)
    scanner_haptics = Column(Boolean, nullable=False)
    scanner_timeout = Column(Integer, nullable=False)

    user = relationship("User", uselist=False, back_populates="user_preference")

    def __init__(self, app_lighting: str = 'System', language: str = 'English',
                 scanner_haptics: bool = True, scanner_timeout: int = 10):
        self.id = uuid4()
        self.app_lighting = app_lighting
        self.language = language
        self.scanner_haptics = scanner_haptics
        self.scanner_timeout = scanner_timeout

class AppLightingPreference(Enum):
    system = 'System'
    light = 'Light'
    dark = 'Dark'

class LanguagePreference(Enum):
    english = 'English'
    deutsch = 'Deutsch'
