from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.ext.declarative import declarative_base

HardwareBase = declarative_base()

class StockStatus(Enum):
    out_of_stock = 1
    ordered = 2
    parts_available = 3

class BuildStatus(Enum):
    not_started = 1
    building = 2
    built = 3
    sent_to_customer = 4

class Hardware(HardwareBase):
    __tablename__ = 'hardware'
    id = Column(UUID(as_uuid=True), primary_key=True)
    order_number = Column(Integer, default=None)
    serial_number = Column(String(40), nullable=False)
    stock_status = Column(String(50), nullable=False)
    build_status = Column(String(50), nullable=False)
    hardware_model_id = Column(UUID(as_uuid=True), nullable=False)
    set_number = Column(Integer)

    def __init__(self, order_number: int, serial_number: str,
                 stock_status: StockStatus, build_status: BuildStatus,
                 hardware_model_id: UUID, set_number: int = None):
        self.id = uuid4()
        self.order_number = order_number
        self.serial_number = serial_number
        self.stock_status = stock_status.name
        self.build_status = build_status.name
        self.hardware_model_id = hardware_model_id
        self.set_number = set_number
