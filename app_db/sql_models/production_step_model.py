from uuid import uuid4

from sqlalchemy import Column, String, UUID, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class ProductionStepModel(ProductionBase):
    __tablename__ = 'production_step_model_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(40), nullable=False)
    version = Column(Integer, nullable=False)
    step_number = Column(Integer, nullable=False)

    production_step = relationship('ProductionStep', uselist=False, back_populates='production_step_model')

    equipment_id = Column(UUID(as_uuid=True), ForeignKey('equipment_table.id'))
    equipment = relationship('Equipment', back_populates='production_step_model')

    hardware_model_id = Column(UUID(as_uuid=True), ForeignKey('hardware_model_table.id'))
    hardware_model = relationship('HardwareModel', back_populates='production_step_model')

    parent_id = Column(UUID(as_uuid=True), ForeignKey('production_step_model_table.id'))

    def __init__(self, name: str, step_number: int, hardware_model,
                 equipment, version: int = 1, parent = None):
        self.id = uuid4()
        self.name = name
        self.version = version
        self.step_number = step_number

        self.hardware_model = hardware_model
        self.hardware_model_id = hardware_model.id

        self.equipment = equipment
        self.equipment_id = equipment.id

        if parent is None:
            self.parent_id = None
        else:
            self.parent_id = parent.id
