from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

from .user import User
from .hardware import Hardware

class ProductionStepStatus(Enum):
    not_started = 'Not Started'
    in_progress = 'In Progress'
    complete = 'Complete'
    paused = 'Paused'
    stopped = 'Stopped'
    abandoned = 'Abandoned'

class ProductionStep(ProductionBase):
    __tablename__ = 'production_step_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(40), nullable=False)
    status = Column(String(50), nullable=False)
    start_timestamp = Column(DateTime, nullable=False)

    measurement = relationship('Measurement', uselist=False, back_populates='production_step')
    picture = relationship('Picture', uselist=False, back_populates='production_step')

    hardware_id = Column(UUID(as_uuid=True), ForeignKey('hardware_table.id'))
    hardware = relationship('Hardware', back_populates='production_step')

    production_step_model_id = Column(UUID(as_uuid=True), ForeignKey('production_step_model_table.id'))
    production_step_model = relationship('ProductionStepModel', back_populates='production_step')

    operator_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    operator = relationship('User', back_populates='production_step_operator')

    def __init__(self, name: str, status: ProductionStepStatus, hardware: Hardware,
                 operator: User, production_step_model):
        self.id = uuid4()
        self.name = name
        self.status = status.value

        self.hardware = hardware
        self.hardware_id = hardware.id

        self.operator = operator
        self.operator_id = operator.id

        self.production_step_model = production_step_model
        self.production_step_model_id = production_step_model.id
