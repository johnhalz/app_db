from uuid import uuid4
from pathlib import Path
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime
from sqlalchemy.ext.declarative import declarative_base

ResultBase = declarative_base()

class Result(ResultBase):
    __tablename__ = 'results'
    id = Column(UUID(as_uuid=True), primary_key=True)
    hardware_id = Column(UUID(as_uuid=True), nullable=False)
    specification_id = Column(UUID(as_uuid=True), nullable=False)
    creation_timestamp = Column(DateTime, nullable=False)
    result_file = Column(String(300), nullable=False)

    def __init__(self, hardware_id: UUID, specification_id: UUID,
                 creation_timestamp: datetime, result_file: Path):
        self.id = uuid4()
        self.hardware_id = hardware_id
        self.specification_id = specification_id
        self.creation_timestamp = creation_timestamp
        self.result_file = result_file.as_posix()
