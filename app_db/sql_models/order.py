from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, Integer, UUID, String, ForeignKey, func
from sqlalchemy.orm import relationship
func: callable

from app_db.interface import AUProductionDB
from .bases import ProductionBase

class OrderType(Enum):
    ASSEMBLY = 'Assembly'
    REPAIR = 'Repair'
    MAINTENANCE = 'Maintenance'

class Order(ProductionBase):
    __tablename__ = 'order_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    number = Column(Integer, nullable=False)
    hardware_id = Column(UUID(as_uuid=True), ForeignKey('hardware_table.id'), nullable=False)
    order_type_string = Column(String(30), nullable=False, default='Assembly')

    hardware = relationship('Hardware', foreign_keys=[hardware_id])

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.order_number = self.generate_new_order_number()

    @classmethod
    def generate_new_order_number(cls) -> int:
        database = AUProductionDB(ip_address='127.0.0.1', port_number=3306, username='root', password='Password123!')
        database.connect('production')
        max_order_number = database.session.query(func.max(cls.number)).scalar()
        database.disconnect()

        if max_order_number is None:
            return 1
        else:
            return max_order_number + 1

    @property
    def order_type(self) -> OrderType:
        return OrderType(self.order_type_string)
