from uuid import uuid4
from sqlalchemy import Column, String, UUID, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

SpecificationBase = declarative_base()

class Specification(SpecificationBase):
    __tablename__ = 'specifications'
    id = Column(UUID, primary_key=True, default=uuid4())
    name = Column(String(40), nullable=False)
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    unit = Column(String(20), nullable=True, default=None)
    material_number = Column(String(40), default='all', nullable=False)
    version = Column(Integer, default=1, nullable=False)
    measurement_id = Column(UUID, nullable=False)
