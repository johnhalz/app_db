from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, UUID, DateTime, Integer

from .bases import ProductionBase


class Result(ProductionBase):
    __tablename__ = 'result_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    creation_timestamp = Column(DateTime, nullable=False, default=datetime.now)
    result_file = Column(String(500), nullable=False)
    version = Column(Integer, nullable=False, default=1)
    processor_commit_hash = Column(String(40), nullable=False)
