from uuid import uuid4
from sqlalchemy import Column, String, UUID
from sqlalchemy.ext.declarative import declarative_base

ProductionStepBase = declarative_base()

class ProductionStep(ProductionStepBase):
    __tablename__ = 'production_steps'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(40), nullable=False)
    material_number = Column(String(40), nullable=False)
    equipment_id = Column(UUID(as_uuid=True))
    operator_id = Column(UUID(as_uuid=True))
    parent_id = Column(UUID(as_uuid=True))

    def __init__(self, name: str, material_number: str, equipment_id: UUID, operator_id: UUID, parent_id: UUID = None):
        self.id = uuid4()
        self.name = name
        self.material_number = material_number
        self.equipment_id = equipment_id
        self.operator_id = operator_id
        self.parent_id = parent_id
