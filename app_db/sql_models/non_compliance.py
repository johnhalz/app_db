from uuid import uuid4
from shortuuid import ShortUUID
from sqlalchemy import Column, String, UUID, Float
from sqlalchemy.ext.declarative import declarative_base

NonComplianceBase = declarative_base()

class NonCompliance(NonComplianceBase):
    __tablename__ = 'non_compliances'
    id = Column(UUID, primary_key=True, default=uuid4())
    short_id = Column(String(4), default=ShortUUID().random(length=4), nullable=False)
    spec_id = Column(UUID, nullable=False)
    result_id = Column(UUID, nullable=False)
    status = Column(String(50), nullable=False)
    decision = Column(String(400), default='')
    comments = Column(String(400), default='')
    reporter_id = Column(UUID, nullable=False)
    signer_id = Column(UUID)
