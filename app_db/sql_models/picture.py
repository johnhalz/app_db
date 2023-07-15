from uuid import uuid4
from pathlib import Path
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class Picture(ProductionBase):
    __tablename__ = 'picture_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    photo_path = Column(String(500), nullable=False)
    creation_timestamp = Column(DateTime, nullable=False, default=datetime.now)

    production_step_id = Column(UUID(as_uuid=True), ForeignKey('production_step_table.id'))
    production_step = relationship('ProductionStep', foreign_keys=[production_step_id])
