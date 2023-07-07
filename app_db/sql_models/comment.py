from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class Comment(ProductionBase):
    __tablename__ = 'comment_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    content = Column(String(500), nullable=False)

    parent_id = Column(UUID(as_uuid=True), ForeignKey('comment_table.id'))
    child_comments = relationship('Comment', backref='parent', remote_side=[id])

    author_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    author = relationship('User', uselist=False, back_populates='comments')

    non_compliance_id = Column(UUID(as_uuid=True), ForeignKey('non_compliance_table.id'))
    non_compliance = relationship('NonCompliance', back_populates='comment')

    def __init__(self, author, content: str, non_compliance, parent = None):
        self.id = uuid4()
        self.content = content
        self.parent = parent
        self.non_compliance = non_compliance

        self.author = author
        self.author_id = author.id
