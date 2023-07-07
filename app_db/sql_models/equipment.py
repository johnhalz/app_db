from uuid import uuid4
from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, UUID, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class EquipmentStatus(Enum):
    in_use = 'In Use'
    not_in_use = 'Not in Use'
    free_to_use = 'Free to Use'
    in_calibration = 'In Calibration'

class Equipment(ProductionBase):
    __tablename__ = 'equipment_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    calibration_timestamp = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)

    parent_id = Column(UUID(as_uuid=True), ForeignKey('equipment_table.id'))
    parent = relationship('Equipment', backref='parent', remote_side=[id])

    production_step_model = relationship('ProductionStepModel', uselist=False, back_populates='equipment')

    def __init__(self, name: str, calibration_timestamp: datetime,
                 status: EquipmentStatus, number: int = 1, parent = None):
        self.id = uuid4()
        self.name = name
        self.number = number
        self.calibration_timestamp = calibration_timestamp
        self.status = status.value
        self.parent = parent
