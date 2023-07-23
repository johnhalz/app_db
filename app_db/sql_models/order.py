from .bases import ProductionBase
from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, Integer, UUID, String, ForeignKey
from sqlalchemy.orm import relationship


class OrderType(Enum):
    ASSEMBLY = 'Assembly'
    REPAIR = 'Repair'
    MAINTENANCE = 'Maintenance'


class Order(ProductionBase):
    __tablename__ = 'order_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    number = Column(Integer, nullable=False)
    hardware_id = Column(
        UUID(as_uuid=True),
        ForeignKey('hardware_table.id'),
        nullable=False
    )
    order_type_string = Column(String(30), nullable=False, default='Assembly')

    hardware = relationship('Hardware', foreign_keys=[hardware_id])

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.order_number = self.generate_new_order_number()

    @property
    def order_type(self) -> OrderType:
        return OrderType(self.order_type_string)
