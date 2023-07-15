from uuid import uuid4

from sqlalchemy import Column, String, UUID, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class ProductionStepModel(ProductionBase):
    __tablename__ = 'production_step_model_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(40), nullable=False)
    version = Column(Integer, nullable=False, default=1)
    step_number = Column(Integer, nullable=False)

    equipment_id = Column(UUID(as_uuid=True), ForeignKey('equipment_table.id'))
    equipment = relationship('Equipment', foreign_keys=[equipment_id])

    hardware_model_id = Column(UUID(as_uuid=True), ForeignKey('hardware_model_table.id'))
    hardware_model = relationship('HardwareModel', foreign_keys=[hardware_model_id])

    parent_id = Column(UUID(as_uuid=True), ForeignKey('production_step_model_table.id'), nullable=True, default=None)
    parent = relationship('ProductionStepModel', foreign_keys=[parent_id])
