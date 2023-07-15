from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class ProductionStepModelWatch(ProductionBase):
    __tablename__ = 'order_watch_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    production_step_model_id = Column(UUID(as_uuid=True), ForeignKey('production_step_model_table.id'), nullable=False)
    production_step_model = relationship('ProductionStepModel', foreign_keys=[production_step_model_id])

    user_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'), nullable=False)
    user = relationship('User', foreign_keys=[user_id])
