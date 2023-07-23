from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase


class OrderWatch(ProductionBase):
    __tablename__ = 'order_watch_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id = Column(
        UUID(as_uuid=True),
        ForeignKey('order_table.id'),
        nullable=False
    )
    order = relationship('Order', foreign_keys=[order_id])
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('user_table.id'),
        nullable=False
    )
    user = relationship('User', foreign_keys=[user_id])
