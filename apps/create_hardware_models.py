import logging
from typing import List
from random import randint, choice

from app_db.interface import AUProductionDB
from app_db.hardware_model import ModelCreator, MirrorType, MGCSize, VCMSize
from app_db.sql_models import HardwareModel

def setup_logger():
    '''Setup logger for app'''
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
        format='[%(asctime)s] %(levelname)-9s %(message)s'
    )

def create_model(mirror: MirrorType, position: int, version: int) -> List[HardwareModel]:
    '''
    Create a single AU model instance

    Parameters
    ----------
    - `mirror` (`MirrorType`): Mirror type
    - `version` (`int`): Version of AU
    - `position` (`int`): Position of AU on assigned mirror

    Returns
    -------
    - `List[HardwareModel]`: List of hardware models to put into database
    '''
    creator = ModelCreator(mirror, version)
    match mirror:
        case MirrorType.M1:
            mgc_size = MGCSize.Medium
            if position == 2:
                mgc_size = MGCSize.Small

            return creator.create_au(str(position), mgc_size, VCMSize.Normal)

        case MirrorType.M2:
            mgc_size = MGCSize.Medium
            if position == 1:
                mgc_size = MGCSize.Small

            return creator.create_au(str(position), mgc_size, VCMSize.Normal)

        case MirrorType.M3:
            return creator.create_au(str(position), MGCSize.Medium, VCMSize.Normal)

        case MirrorType.M4:
            if position in [1, 2, 3]:
                return creator.create_au(str(position), vcm_size=VCMSize.Normal, without_mgc=True)

            else:
                return creator.create_au(str(position), mgc_size=MGCSize.Large, without_vcm=True)

        case MirrorType.M5:
            return creator.create_au(str(position), MGCSize.Medium, VCMSize.Normal)

        case MirrorType.M6:
            mgc_size = MGCSize.Medium
            if position == 1:
                mgc_size = MGCSize.Small

            return creator.create_au(str(position), mgc_size, vcm_size=VCMSize.Normal)

        case MirrorType.M7:
            return creator.create_au(str(position), MGCSize.Small, VCMSize.Normal)

        case MirrorType.M8:
            if position in [1, 2, 3]:
                return creator.create_au(str(position), vcm_size=VCMSize.Large, without_mgc=True)

            else:
                return creator.create_au(str(position), mgc_size=MGCSize.Large, without_vcm=True)

        case MirrorType.RSMF:
            return creator.create_au(str(position), MGCSize.Medium, VCMSize.Normal)

def main():
    pass

if __name__ == '__main__':
    setup_logger()
    main()
