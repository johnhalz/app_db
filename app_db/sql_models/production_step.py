from uuid import uuid4
from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase


class ProductionStepStatus(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    COMPLETE = 'Complete'
    PAUSED = 'Paused'
    STOPPED = 'Stopped'
    ABANDONED = 'Abandoned'


class ProductionStep(ProductionBase):
    __tablename__ = 'production_step_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(40), nullable=False)
    status_string = Column(String(50), nullable=False, default='Not Started')
    start_timestamp = Column(DateTime, nullable=False, default=datetime.now)

    order_id = Column(UUID(as_uuid=True), ForeignKey('order_table.id'))
    order = relationship('Order', foreign_keys=[order_id])

    production_step_model_id = Column(
        UUID(as_uuid=True),
        ForeignKey('production_step_model_table.id')
    )
    production_step_model = relationship(
        'ProductionStepModel',
        foreign_keys=[production_step_model_id]
    )

    operator_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    operator = relationship('User', foreign_keys=[operator_id])

    @property
    def status(self) -> ProductionStepStatus:
        return ProductionStepStatus(self.status_string)
