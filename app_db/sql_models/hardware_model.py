from uuid import uuid4

from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.ext.declarative import declarative_base

HardwareModelBase = declarative_base()

class HardwareModel(HardwareModelBase):
    __tablename__ = 'hardware_models'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(50), nullable=False)
    position = Column(String(50))
    parent_id = Column(UUID(as_uuid=True))
    version = Column(Integer, nullable=False)
    mirror = Column(Integer, nullable=False)

    def __init__(self, name: str, version: int, mirror: int, position: str = None, parent_id: UUID = None):
        self.id = uuid4()
        self.name = name
        self.version = version
        self.mirror = mirror
        self.position = position
        self.parent_id = parent_id
