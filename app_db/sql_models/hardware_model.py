from uuid import uuid4

from sqlalchemy import Column, String, UUID, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase
# from app_db.hardware_types import MirrorType

class HardwareModel(ProductionBase):
    __tablename__ = 'hardware_model_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(50), nullable=False)
    position = Column(String(50))
    version = Column(Integer, nullable=False)
    mirror = Column(Integer, nullable=False)

    parent_id = Column(UUID(as_uuid=True), ForeignKey('hardware_model_table.id'))
    parent = relationship('HardwareModel', backref='parent', remote_side=[id])

    hardware = relationship('Hardware', uselist=False, back_populates='hardware_model')

    def __init__(self, name: str, version: int, mirror, position: str = None, parent = None):
        self.id = uuid4()
        self.name = name
        self.version = version
        self.mirror = mirror.value
        self.position = position
        self.parent = parent
