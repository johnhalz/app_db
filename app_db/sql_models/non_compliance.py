from enum import Enum

from shortuuid import ShortUUID
from sqlalchemy import Column, String, UUID

from .bases import ProductionBase

class NonComplianceStatus(Enum):
    not_started = 1
    in_review = 2
    abandoned = 3
    resolved = 4

class NonCompliance(ProductionBase):
    __tablename__ = 'non_compliances'

    id = Column(String(6), primary_key=True, nullable=False)
    spec_id = Column(UUID(as_uuid=True), nullable=False)
    result_id = Column(UUID(as_uuid=True), nullable=False)
    status = Column(String(50), nullable=False)
    decision = Column(String(400))
    reporter_id = Column(UUID(as_uuid=True), nullable=False)
    signer_id = Column(UUID(as_uuid=True))

    def __init__(self, spec_id: UUID, result_id: UUID, reporter_id: UUID, signer_id: UUID,
                 status: NonComplianceStatus = NonComplianceStatus.not_started,
                 decision: str = '', comments: str = ''):
        self.id = ShortUUID().random(length=6)
        self.spec_id = spec_id
        self.result_id = result_id
        self.reporter_id = reporter_id
        self.signer_id = signer_id
        self.status = status.name
        self.decision = decision
        self.comments = comments
