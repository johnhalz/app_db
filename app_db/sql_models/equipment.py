from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, UUID, Integer, DateTime

from .bases import ProductionBase

class Equipment(ProductionBase):
    __tablename__ = 'equipment'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    calibration_timestamp = Column(DateTime, nullable=False)
    parent_id = Column(UUID(as_uuid=True))

    def __init__(self, name: str, calibration_timestamp: datetime, number: int = 1, parent_id: UUID = None):
        self.id = uuid4()
        self.name = name
        self.number = number
        self.calibration_timestamp = calibration_timestamp,
        self.parent_id = parent_id
