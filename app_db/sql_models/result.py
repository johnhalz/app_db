from uuid import uuid4
from pathlib import Path
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class Result(ProductionBase):
    __tablename__ = 'result_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(100), nullable=False)
    creation_timestamp = Column(DateTime, nullable=False)
    result_file = Column(String(500), nullable=False)
    version = Column(Integer, nullable=False)

    non_compliance = relationship('NonCompliance', uselist=False, back_populates='result')

    hardware_id = Column(UUID(as_uuid=True), ForeignKey('hardware_table.id'))
    hardware = relationship('Hardware', back_populates='result')

    specification_id = Column(UUID(as_uuid=True), ForeignKey('specification_table.id'))
    specification = relationship('Specification', back_populates='result')

    measurement_id = Column(UUID(as_uuid=True), ForeignKey('measurement_table.id'))
    measurement = relationship('Measurement', back_populates='result')

    def __init__(self, name: str, hardware, specification, measurement,
                 result_file: Path, version: int, creation_timestamp: datetime = datetime.now()):
        self.id = uuid4()
        self.creation_timestamp = creation_timestamp
        self.result_file = result_file.as_posix()
        self.version = version
        self.name = name

        self.hardware = hardware
        self.hardware_id = self.hardware.id

        self.specification = specification
        self.specification_id = self.specification.id

        self.measurement = measurement
        self.measurement_id = measurement.id
