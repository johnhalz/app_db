from uuid import uuid4

from sqlalchemy import Column, String, UUID, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase
from .hardware_model import HardwareModel

class Specification(ProductionBase):
    __tablename__ = 'specification_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(40), nullable=False)
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    unit = Column(String(20), nullable=True)
    version = Column(Integer, nullable=False)
    description = Column(String(500))

    result = relationship('Result', uselist=False, back_populates='specification')

    hardware_model_id = Column(UUID(as_uuid=True), ForeignKey('hardware_model_table.id'), nullable=False)
    hardware_model = relationship('HardwareModel', back_populates='specification')

    def __init__(self, name: str, min_value: float, max_value: float, hardware_model: HardwareModel,
                 description: str = None, unit: str = None, version: int = 1):
        self.id = uuid4()
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.unit = unit
        self.version = version
        self.description = description
        self.hardware_model = hardware_model
        self.hardware_model_id = hardware_model.id
