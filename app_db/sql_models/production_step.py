from uuid import uuid4
from sqlalchemy import Column, String, UUID
from sqlalchemy.ext.declarative import declarative_base

ProductionStepBase = declarative_base()

class ProductionStep(ProductionStepBase):
    __tablename__ = 'production_steps'
    id = Column(UUID, primary_key=True, default=uuid4())
    name = Column(String(40), nullable=False)
    material_number = Column(String(40), nullable=False)
    equipment_id = Column(UUID)
    operator_id = Column(UUID)
    parent_id = Column(UUID)
