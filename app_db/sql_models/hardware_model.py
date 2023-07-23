from uuid import uuid4

from sqlalchemy import Column, String, UUID, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase


class HardwareModel(ProductionBase):
    __tablename__ = 'hardware_model_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    position = Column(String(50), nullable=True, default=None)
    version = Column(Integer, nullable=False)
    mirror = Column(Integer, nullable=False)

    parent_id = Column(
        UUID(as_uuid=True),
        ForeignKey('hardware_model_table.id'),
        nullable=True,
        default=None
    )
    parent = relationship('HardwareModel', foreign_keys=[parent_id])
