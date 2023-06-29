from typing import List, Union
from uuid import UUID

from app_db.hardware_model import MirrorType, MGCSize, VCMSize
from app_db.sql_models import HardwareModel

class ModelCreator:
    def __init__(self, mirror: MirrorType, version: int) -> None:
        self.mirror = mirror
        self.version = version

    def create_au(self, position: str, mgc_size: MGCSize = None, vcm_size: VCMSize = None,
                        without_vcm: bool = False, without_mgc: bool = False) -> List[HardwareModel]:
        if without_vcm:
            return self.create_mgc(size=mgc_size)

        au = self.create_model(name='AU', parent_id=None, position=position)
        support_block = self.create_model(name='Support Block', parent_id=au.id)
        vcm1 = self.create_vcm(size=vcm_size, parent_id=au.id, position='1')
        vcm2 = self.create_vcm(size=vcm_size, parent_id=au.id, position='2')

        hw_models = [au, support_block] + vcm1 + vcm2

        if not without_mgc:
            mgc = self.create_mgc(size=mgc_size, parent_id=au.id)
            hw_models += mgc

        return hw_models

    def create_mgc(self, size: MGCSize, parent_id: UUID = None) -> List[HardwareModel]:
        mgc = self.create_model(name=f'MGC - {size.name[0]}', parent_id=parent_id)
        housing = self.create_model(name='Housing', parent_id=mgc.id)
        magnet = self.create_model(name='Magnet', parent_id=mgc.id)
        tmds = self.create_model(name='TMD', parent_id=mgc.id, quantity=2)

        hw_models = [mgc, housing, magnet]
        hw_models = hw_models.extend(tmds)
        return hw_models

    def create_vcm(self, size: VCMSize, parent_id: UUID, position: str) -> List[HardwareModel]:
        vcm = self.create_model(name=f'VCM - {size.name[0]}', parent_id=parent_id, position=position)
        housing = self.create_model(name='Housing', parent_id=vcm.id)
        magnet = self.create_model(name='Magnet', parent_id=vcm.id)
        coil = self.create_model(name='Coil', parent_id=vcm.id)
        pcb = self.create_model(name='PCB', parent_id=vcm.id)
        tmds = self.create_model(name='TMD', parent_id=vcm.id, quantity=2)

        hw_models = [vcm, housing, magnet, coil, pcb]
        hw_models = hw_models.extend(tmds)
        return hw_models

    def create_model(self, name: str, parent_id: UUID, position: str = None, quantity: int = 1) \
                    -> Union[List[HardwareModel], HardwareModel]:
        if quantity < 1:
            raise ValueError(
                f'Unable to create hardware models with a quantity of {quantity}.'
            )

        if quantity == 1:
            return HardwareModel(
                name = name,
                parent_id = parent_id,
                position = position,
                version = self.version,
                mirror = self.mirror.value
            )

        else:
            hardware_models = []

            if position is not None:
                position = f'{position} - '

            for i in range(1, quantity+1):
                model = HardwareModel(
                    name = name,
                    parent_id = parent_id,
                    position = f'{position}{i}',
                    version = self.version,
                    mirror = self.mirror.value
                )

                hardware_models.append(model)

            return hardware_models
