from uuid import uuid4
from sqlalchemy import Column, String, UUID, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

UserPreferenceBase = declarative_base()

class UserPreference(UserPreferenceBase):
    __tablename__ = 'user_preferences'
    id = Column(UUID, primary_key=True, default=uuid4())
    app_light_mode = Column(String(10), default='System', nullable=False)
    language = Column(String(10), default='English', nullable=False)
    scanner_haptics = Column(Boolean, default=True, nullable=False)
    scanner_timeout = Column(Integer, default=10, nullable=False)
