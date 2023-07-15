from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class EquipmentStatus(Enum):
    IN_USE = 'In Use'
    NOT_IN_USE = 'Not in Use'
    FREE_TO_USE = 'Free to Use'
    IN_CALIBRATION = 'In Calibration'

class Equipment(ProductionBase):
    __tablename__ = 'equipment_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    calibration_timestamp = Column(DateTime, nullable=False)
    status_string = Column(String(50), nullable=False)

    parent_id = Column(UUID(as_uuid=True), ForeignKey('equipment_table.id'), nullable=True, default=None)
    parent = relationship('Equipment', foreign_keys=[parent_id])

    @property
    def status(self) -> EquipmentStatus:
        return EquipmentStatus(self.status_string)
