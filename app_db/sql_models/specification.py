from uuid import uuid4
from enum import Enum

from astropy.units import Quantity

from sqlalchemy import Column, String, UUID, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .bases import ProductionBase

class SpecificationSeverity(Enum):
    CAN_BE_IGNORED = 'Can be Ignored'
    VERY_LOW = 'Very Low'
    LOW = 'Low'
    NORMAL = 'Normal'
    HIGH = 'High'
    VERY_HIGH = 'Very High'
    HIGHEST = 'Highest'
    CRITICAL = 'Critical'

class Specification(ProductionBase):
    __tablename__ = 'specification_table'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(40), nullable=False)
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    unit_string = Column(String(20), nullable=False, default='')
    version = Column(Integer, nullable=False, default=1)
    description = Column(String(500), nullable=True, default=None)
    severity_string = Column(String(50), nullable=False, default='Normal')

    hardware_model_id = Column(UUID(as_uuid=True), ForeignKey('hardware_model_table.id'), nullable=False)
    hardware_model = relationship('HardwareModel', foreign_keys=[hardware_model_id])

    production_step_model_id = Column(UUID(as_uuid=True), ForeignKey('production_step_model.id'), nullable=False)
    production_step_model = relationship('ProductionStepModel', foreign_keys=[production_step_model_id])

    @property
    def minimum(self) -> Quantity:
        return Quantity(self.min_value, self.unit_string)

    @property
    def maximum(self) -> Quantity:
        return Quantity(self.max_value, self.unit_string)

    @property
    def severity(self) -> SpecificationSeverity:
        return SpecificationSeverity(self.severity_string)

    def is_validated_by(self, input: Quantity, including_boundaries: bool = True) -> bool:
        if including_boundaries:
            return self.minimum <= input <= self.maximum
        else:
            return self.minimum < input < self.maximum
