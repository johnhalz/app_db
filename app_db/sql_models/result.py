from uuid import uuid4
from sqlalchemy import Column, String, UUID, DateTime
from sqlalchemy.ext.declarative import declarative_base

ResultBase = declarative_base()

class Result(ResultBase):
    __tablename__ = 'results'
    id = Column(UUID, primary_key=True, default=uuid4())
    hardware_id = Column(UUID, nullable=False)
    specification_id = Column(UUID, nullable=False)
    creation_timestamp = Column(DateTime, nullable=False)
    result_file = Column(String(300), nullable=False)
