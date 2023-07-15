from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class MeasurementResultJunction(ProductionBase):
    __tablename__ = 'measurement_result_junction_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    measurement_id = Column(UUID(as_uuid=True), ForeignKey('measurement_table.id'))
    measurement = relationship('Measurement', foreign_keys=[measurement_id])

    result_id = Column(UUID(as_uuid=True), ForeignKey('result_table.id'))
    result = relationship('Result', foreign_keys=[result_id])
