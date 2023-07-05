from uuid import uuid4
from sqlalchemy import Column, String, UUID

from .bases import ProductionBase

from .user import User
from .equipment import Equipment
from .hardware import Hardware

class ProductionStep(ProductionBase):
    __tablename__ = 'production_steps'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(40), nullable=False)
    hardware_id = Column(UUID(as_uuid=True), nullable=False)
    equipment_id = Column(UUID(as_uuid=True))
    operator_id = Column(UUID(as_uuid=True), nullable=False)
    parent_id = Column(UUID(as_uuid=True))

    # hardware: Hardware = None
    # equipment: Equipment = None
    # operator: User = None

    def __init__(self, name: str, hardware: Hardware, equipment: Equipment, operator: User, parent_id: UUID = None):
        self.id = uuid4()
        self.name = name
        self.parent_id = parent_id

        # self.equipment = equipment
        # self.equipment_id = self.equipment.id

        # self.operator = operator
        # self.operator_id = self.operator.id

        # self.hardware = hardware
        # self.hardware_id = self.hardware.id
