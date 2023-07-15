from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class StockStatus(Enum):
    OUT_OF_STOCK = 'Out of Stock'
    ORDERED = 'Ordered'
    PARTS_AVAILABLE = 'Parts Available'

class BuildStatus(Enum):
    NOT_STARTED = 'Not Started'
    BUILDING = 'Building'
    BUILT = 'Built'
    SENT_TO_CUSTOMER = 'Sent to Customer'
    RETURNED_FROM_CUSTOMER = 'Returned from Customer'

class Hardware(ProductionBase):
    __tablename__ = 'hardware_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    serial_number = Column(String(40), nullable=False)
    stock_status_string = Column(String(50), nullable=False)
    build_status_string = Column(String(50), nullable=False)
    set_number = Column(Integer, nullable=True, default=None)

    hardware_model_id = Column(UUID(as_uuid=True), ForeignKey('hardware_model_table.id'))
    hardware_model = relationship('HardwareModel', foreign_keys=[hardware_model_id])

    @property
    def stock_status(self) -> StockStatus:
        return StockStatus(self.stock_status_string)

    @property
    def build_status(self) -> BuildStatus:
        return BuildStatus(self.build_status_string)
