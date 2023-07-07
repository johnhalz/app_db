from enum import Enum
from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

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
    description = Column(String(500))
    decision = Column(String(500))

    comment = relationship('Comment', back_populates='non_compliance')

    result_id = Column(UUID(as_uuid=True), ForeignKey('result_table.id'))
    result = relationship('Result', uselist=False, back_populates='non_compliance')

    reporter_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    reporter = relationship('User', uselist=False, back_populates='non_compliance_reporter', foreign_keys=[reporter_id])

    signer_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    signer = relationship('User', uselist=False, back_populates='non_compliance_signer', foreign_keys=[signer_id])

    def __init__(self, status: NonComplianceStatus, result, reporter,
                 signer = None, decision: str = '', description: str = ''):
        self.id = uuid4()
        self.status = status.value
        self.decision = decision
        self.description = description

        self.result = result
        self.result_id = result.id

        self.reporter = reporter
        self.reporter_id = reporter.id

        self.signer = signer
        self.signer_id = signer.id

    @property
    def short_id(self) -> str:
        return str(self.id.fields[1])

