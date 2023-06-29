from uuid import uuid4

from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.ext.declarative import declarative_base

HardwareModelBase = declarative_base()

class HardwareModel(HardwareModelBase):
    __tablename__ = 'hardware_models'
    id = Column(UUID, primary_key=True, default=uuid4())
    name = Column(String(50), nullable=False)
    position = Column(String(50))
    parent_id = Column(UUID, default=None)
    version = Column(Integer, nullable=False)
    mirror = Column(Integer, nullable=False)
