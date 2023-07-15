from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class SpecificationResultJunction(ProductionBase):
    __tablename__ = 'specification_result_junction_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    specification_id = Column(UUID(as_uuid=True), ForeignKey('specification_table.id'))
    specification = relationship('Specification', foreign_keys=[specification_id])

    result_id = Column(UUID(as_uuid=True), ForeignKey('result_table.id'))
    result = relationship('Result', foreign_keys=[result_id])
