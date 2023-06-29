from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID
from sqlalchemy.ext.declarative import declarative_base

MeasurementBase = declarative_base()

class Measurement(MeasurementBase):
    __tablename__ = 'measurements'
    id = Column(UUID, primary_key=True, default=uuid4())
    name = Column(String(60), nullable=False)
    measurement_type = Column(String(50), nullable=False)

class MeasurementType(Enum):
    list = 1
    array = 2
    single = 3
