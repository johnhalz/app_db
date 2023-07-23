from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase


class Comment(ProductionBase):
    __tablename__ = 'comment_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    content = Column(String(500), nullable=False)

    parent_id = Column(UUID(as_uuid=True), ForeignKey('comment_table.id'))
    parent = relationship('Comment', foreign_keys=[parent_id])

    author_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    author = relationship('User', foreign_keys=[author_id])

    non_compliance_id = Column(
        UUID(as_uuid=True),
        ForeignKey('non_compliance_table.id')
    )
    non_compliance = relationship(
        'NonCompliance',
        foreign_keys=[non_compliance_id]
    )
