from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase
from .user import User

class Comment(ProductionBase):
    __tablename__ = 'comment_table'

    id = Column(UUID(as_uuid=True), primary_key=True)
    content = Column(String(500), nullable=False)

    parent_id = Column(UUID(as_uuid=True), ForeignKey('comment_table.id'))
    parent = relationship('Comment', backref='parent', remote_side=[id])

    author_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    author = relationship('User', back_populates='user')

    def __init__(self, author: User, content: String, parent = None):
        self.id = uuid4()
        self.content = content
        self.parent = parent

        self.author = author
        self.author_id = author.id
