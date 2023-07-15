from enum import Enum
from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class NonComplianceStatus(Enum):
    NOT_REVIEWED = 'Not Reviewed'
    IN_REVIEW = 'In Review'
    FIX_IN_PROGRESS = 'Fix in Progress'
    RESOLVED = 'Resolved'
    ABANDONED = 'Abandoned'

class NonCompliance(ProductionBase):
    __tablename__ = 'non_compliance_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    status_string = Column(String(50), nullable=False)
    description = Column(String(1000), default='')
    decision = Column(String(500), default='')

    result_id = Column(UUID(as_uuid=True), ForeignKey('result_table.id'))
    result = relationship('Result', foreign_keys=[result_id])

    reporter_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    reporter = relationship('User', foreign_keys=[reporter_id])

    signer_id = Column(UUID(as_uuid=True), ForeignKey('user_table.id'))
    signer = relationship('User', foreign_keys=[signer_id])

    @property
    def short_id(self) -> str:
        return str(self.id.fields[1])

    @property
    def status(self) -> NonComplianceStatus:
        return NonComplianceStatus(self.status_string)
