from uuid import uuid4
from sqlalchemy import Column, String, UUID, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

UserPreferenceBase = declarative_base()

class UserPreference(UserPreferenceBase):
    __tablename__ = 'user_preferences'
    id = Column(UUID(as_uuid=True), primary_key=True)
    app_light_mode = Column(String(10), nullable=False)
    language = Column(String(10), nullable=False)
    scanner_haptics = Column(Boolean, nullable=False)
    scanner_timeout = Column(Integer, nullable=False)

    def __init__(self, app_light_mode: str = 'System', language: str = 'English',
                 scanner_haptics: bool = True, scanner_timeout: int = 10):
        self.id = uuid4()
        self.app_light_mode = app_light_mode
        self.language = language
        self.scanner_haptics = scanner_haptics
        self.scanner_timeout = scanner_timeout
