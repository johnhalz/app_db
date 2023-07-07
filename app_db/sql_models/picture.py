from uuid import uuid4
from pathlib import Path
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class Picture(ProductionBase):
    __tablename__ = 'picture_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    photo_path = Column(String(300), nullable=False)
    creation_timestamp = Column(DateTime, nullable=False)

    hardware_id = Column(UUID(as_uuid=True), ForeignKey('hardware_table.id'))
    hardware = relationship('Hardware', uselist=False, back_populates='picture')

    production_step_id = Column(UUID(as_uuid=True), ForeignKey('production_step_table.id'))
    production_step = relationship('ProductionStep', uselist=False, back_populates='picture')

    def __init__(self, hardware, production_step,
                 photo_path: Path, creation_timestamp: datetime = datetime.now()):
        self.id = uuid4()
        self.creation_timestamp = creation_timestamp
        self.photo_path = photo_path.as_posix()

        self.hardware = hardware
        self.hardware_id = hardware.id

        self.production_step = production_step
        self.production_step_id = production_step.id
