from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class StockStatus(Enum):
    out_of_stock = 'Out of Stock'
    ordered = 'Ordered'
    parts_available = 'Parts Available'

class BuildStatus(Enum):
    not_started = 'Not Started'
    building = 'Building'
    built = 'Built'
    sent_to_customer = 'Sent to Customer'

class Hardware(ProductionBase):
    __tablename__ = 'hardware_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    order_number = Column(Integer, default=None)
    serial_number = Column(String(40), nullable=False)
    stock_status = Column(String(50), nullable=False)
    build_status = Column(String(50), nullable=False)
    set_number = Column(Integer)

    result = relationship('Result', uselist=False, back_populates='hardware')
    production_step = relationship('ProductionStep', uselist=False, back_populates='hardware')
    picture = relationship('Picture', uselist=False, back_populates='hardware')

    hardware_model_id = Column(UUID(as_uuid=True), ForeignKey('hardware_model_table.id'))
    hardware_model = relationship('HardwareModel', uselist=False, back_populates='hardware')

    def __init__(self, order_number: int, serial_number: str,
                 stock_status: StockStatus, build_status: BuildStatus,
                 hardware_model, set_number: int = None):
        self.id = uuid4()
        self.order_number = order_number
        self.serial_number = serial_number
        self.stock_status = stock_status.value
        self.build_status = build_status.value
        self.set_number = set_number

        self.hardware_model = hardware_model
        self.hardware_model_id = hardware_model.id
