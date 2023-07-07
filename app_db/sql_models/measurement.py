from uuid import uuid4
from pathlib import Path
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class Measurement(ProductionBase):
    __tablename__ = 'measurement_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(60), nullable=False)
    measurement_file = Column(String(300), nullable=False)
    creation_timestamp = Column(DateTime, nullable=False)

    result = relationship('Result', uselist=False, back_populates='measurement')

    production_step_id = Column(UUID(as_uuid=True), ForeignKey('production_step_table.id'))
    production_step = relationship('ProductionStep', uselist=False, back_populates='measurement')

    def __init__(self, name: str, measurement_file: Path, production_step,
                 creation_timestamp: datetime = datetime.now()):
        self.id = uuid4()
        self.name = name
        self.measurement_file = measurement_file.as_posix()
        self.creation_timestamp = creation_timestamp

        self.production_step = production_step
        self.production_step_id = production_step.id
