from uuid import uuid4
from pathlib import Path
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime, Integer

from .bases import ProductionBase
from .specification import Specification
from .hardware import Hardware

class Result(ProductionBase):
    __tablename__ = 'results'

    id = Column(UUID(as_uuid=True), primary_key=True)
    hardware_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(100), nullable=False)
    specification_id = Column(UUID(as_uuid=True), nullable=False)
    creation_timestamp = Column(DateTime, nullable=False)
    result_file = Column(String(500), nullable=False)
    version = Column(Integer, nullable=False)

    # specification: Specification = None
    # hardware: Hardware = None

    def __init__(self, hardware: Hardware, specification: Specification,
                 creation_timestamp: datetime, result_file: Path, version: int):
        self.id = uuid4()
        self.creation_timestamp = creation_timestamp
        self.result_file = result_file.as_posix()
        self.version = version

        # self.hardware = hardware
        # self.hardware_id = self.hardware.id

        # self.specification = specification
        # self.specification_id = self.specification.id
