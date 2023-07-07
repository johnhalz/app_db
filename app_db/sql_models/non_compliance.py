from enum import Enum
from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase
from .result import Result
from .user import User

class NonComplianceStatus(Enum):
    not_started = 'Not Started'
    in_review = 'In Review'
    abandoned = 'Abandoned'
    resolved = 'Resolved'
    fix_in_progress = 'Fix in Progress'

class NonCompliance(ProductionBase):
    __tablename__ = 'non_compliance_table'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    status = Column(String(50), nullable=False)
    decision = Column(String(400))

    comment = relationship('Comment', back_populates='non_compliance')

    result_id = Column(UUID(as_uuid=True), ForeignKey('specification_table.id'))
    result = relationship('Result', back_populates='non_compliance')

    reporter_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    reporter = relationship('User', back_populates='non_compliance')

    signer_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    signer = relationship('User', back_populates='non_compliance')

    def __init__(self, status: NonComplianceStatus, result: Result, reporter: User, signer: User = None, decision: str = ''):
        self.id = uuid4()
        self.status = status.value

        self.result = result
        self.result_id = result.id

        self.reporter = reporter
        self.reporter_id = reporter.id

        self.signer = signer
        self.signer_id = signer.id

        self.decision = decision
