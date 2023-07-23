from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, Boolean, Integer, UUID

from .bases import ProductionBase


class AppLightingPreference(Enum):
    SYSTEM = 'System'
    LIGHT = 'Light'
    DARK = 'Dark'


class LanguagePreference(Enum):
    ENGLISH = 'English'
    DEUTSCH = 'Deutsch'


class UserPreference(ProductionBase):
    __tablename__ = 'user_preference_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    app_lighting_string = Column(String(10), nullable=False, default='System')
    language_string = Column(String(10), nullable=False, default='English')
    scanner_haptics = Column(Boolean, nullable=False, default=True)
    scanner_timeout = Column(Integer, nullable=False, default=10)

    @property
    def app_lighting(self) -> AppLightingPreference:
        return AppLightingPreference(self.app_lighting_string)

    @property
    def language(self) -> LanguagePreference:
        return LanguagePreference(self.language_string)
