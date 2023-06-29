from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.ext.declarative import declarative_base

HardwareBase = declarative_base()

class Hardware(HardwareBase):
    __tablename__ = 'hardware'
    id = Column(UUID, primary_key=True, default=uuid4())
    order_number = Column(Integer, default=None)
    serial_number = Column(String(40), nullable=False)
    stock_status = Column(String(50), nullable=False)
    build_status = Column(String(50), nullable=False)
    hardware_model_id = Column(UUID, nullable=False)

class StockStatus(Enum):
    out_of_stock = 1
    ordered = 2
    parts_available = 3

class BuildStatus(Enum):
    not_started = 1
    building = 2
    built = 3
    sent_to_customer = 4
