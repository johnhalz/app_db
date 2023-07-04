from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.ext.declarative import declarative_base

CommentBase = declarative_base()

class Comment(CommentBase):
    __tablename__ = 'comments'
    id = Column(UUID(as_uuid=True), primary_key=True)
    parent = Column(UUID(as_uuid=True))
    author_id = Column(UUID(as_uuid=True))
    upvotes = Column(Integer, nullable=False)
    content = Column(String(500), nullable=False)

    def __init__(self, parent: UUID, author_id: UUID, content: String, upvotes: int = 0):
        self.id = uuid4()
        self.parent = parent
        self.author_id = author_id
        self.content = content
        self.upvotes = upvotes
