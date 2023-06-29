from uuid import uuid4
from sqlalchemy import Column, String, UUID, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

SpecificationBase = declarative_base()

class Specification(SpecificationBase):
    __tablename__ = 'specifications'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(40), nullable=False)
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    unit = Column(String(20), nullable=True)
    material_number = Column(String(40), nullable=False)
    version = Column(Integer, nullable=False)
    measurement_id = Column(UUID(as_uuid=True), nullable=False)

    def __init__(self, name: str, min_value: float, max_value: float, measurement_id: UUID,
                 unit: str = None, material_number: str = 'all', version: int = 1):
        self.id = uuid4()
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.unit = unit
        self.material_number = material_number
        self.version = version
        self.measurement_id = measurement_id
