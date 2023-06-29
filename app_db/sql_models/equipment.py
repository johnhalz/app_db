from uuid import uuid4
from sqlalchemy import Column, String, UUID, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

EquipmentBase = declarative_base()

class Equipment(EquipmentBase):
    __tablename__ = 'equipment'
    id = Column(UUID, primary_key=True, default=uuid4())
    name = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False, default=1)
    calibration_timestamp = Column(DateTime, nullable=False)
    parent_id = Column(UUID, default=None)
