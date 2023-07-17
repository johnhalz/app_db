from typing import List, Union

from sqlalchemy.orm import Session

from app_db.sql_models import HardwareModel
from app_db.hardware_types import MirrorType, MGCSize, VCMSize

class ModelCreator:
    def __init__(self, mirror: MirrorType, version: int, session: Session) -> None:
        self.mirror = mirror
        self.version = version
        self.session = session

    def create_au(self, position: str, mgc_size: MGCSize = None, vcm_size: VCMSize = None,
                        without_vcm: bool = False, without_mgc: bool = False) -> List[HardwareModel]:
        if without_vcm:
            return self.create_mgc(size=mgc_size)

        au = self.create_model(name='AU', parent=None, position=position)
        support_block = self.create_model(name='Support Block', parent=au)
        vcm1 = self.create_vcm(size=vcm_size, parent=au, position='1')
        vcm2 = self.create_vcm(size=vcm_size, parent=au, position='2')

        hw_models = []
        hw_models.append(au)
        hw_models.append(support_block)
        hw_models.extend(vcm1)
        hw_models.extend(vcm2)

        if not without_mgc:
            mgc = self.create_mgc(size=mgc_size, parent=au)
            hw_models.extend(mgc)

        return hw_models

    def create_mgc(self, size: MGCSize, parent: HardwareModel = None) -> List[HardwareModel]:
        mgc = self.create_model(name=f'MGC - {size.name[0]}', parent=parent)
        housing = self.create_model(name='Housing', parent=mgc)
        magnet = self.create_model(name='Magnet', parent=mgc)
        tmds = self.create_model(name='TMD', parent=mgc, quantity=2)

        hw_models = []
        hw_models.append(mgc)
        hw_models.append(housing)
        hw_models.append(magnet)
        hw_models.extend(tmds)

        return hw_models

    def create_vcm(self, size: VCMSize, parent: HardwareModel, position: str) -> List[HardwareModel]:
        vcm = self.create_model(name=f'VCM - {size.name[0]}', parent=parent, position=position)
        housing = self.create_model(name='Housing', parent=vcm)
        magnet = self.create_model(name='Magnet', parent=vcm)
        coil = self.create_model(name='Coil', parent=vcm)
        pcb = self.create_model(name='PCB', parent=vcm)
        tmds = self.create_model(name='TMD', parent=vcm, quantity=2)

        hw_models = []
        hw_models.append(vcm)
        hw_models.append(housing)
        hw_models.append(magnet)
        hw_models.append(coil)
        hw_models.append(pcb)
        hw_models.extend(tmds)
        return hw_models

    def create_model(self, name: str, parent: HardwareModel,
                     position: str = None, quantity: int = 1):
        if quantity < 1:
            raise ValueError(
                f'Unable to create hardware models with a quantity of {quantity}.'
            )

        if quantity == 1:
            new_model = HardwareModel(
                name = name,
                parent = parent,
                position = position,
                version = self.version,
                mirror = self.mirror,
                parent_id = parent.id
            )
            self.session.add(new_model)
            self.session.commit()

            return new_model

        else:
            hardware_models = []

            if position is not None:
                position = f'{position} - '
            else:
                position = ''

            for i in range(1, quantity+1):
                new_model = HardwareModel(
                    name = name,
                    parent = parent,
                    position = f'{position}{i}',
                    version = self.version,
                    mirror = self.mirror,
                    parent_id = parent.id
                )
                self.session.add(new_model)
                self.session.commit()
                hardware_models.append(new_model)

            return hardware_models
