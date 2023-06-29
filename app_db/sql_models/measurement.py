from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID
from sqlalchemy.ext.declarative import declarative_base

MeasurementBase = declarative_base()

class MeasurementType(Enum):
    single = 1
    array = 1

class Measurement(MeasurementBase):
    __tablename__ = 'measurements'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(60), nullable=False)
    measurement_type = Column(String(50), nullable=False)

    def __init__(self, name: str, measurement_type: MeasurementType = MeasurementType.single):
        self.id = uuid4()
        self.name = name
        self.measurement_type = measurement_type.name
