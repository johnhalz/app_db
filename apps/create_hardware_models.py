import logging
import argparse
from typing import List

from app_db.interface import AUProductionDB
from app_db.hardware_types import ModelCreator, MirrorType, MGCSize, VCMSize
from app_db.sql_models import HardwareModel, ProductionBase

def setup_logger():
    '''Setup logger for app'''
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
        format='[%(asctime)s] %(levelname)-9s %(message)s'
    )

def parse_arguments():
    '''Parse input arguments to app'''
    parser = argparse.ArgumentParser(
        prog='Create Hardware Models',
        description='Create hardware models in database'
    )
    parser.add_argument('-v', '--version',
                        dest='version',
                        type=int,
                        default=1,
                        help='Hardware models version number')

    return parser.parse_args()

def evaluate_args():
    '''Evaluate input arguments'''
    args = parse_arguments()

    return args.version

def valid_positions(mirror: MirrorType) -> List[int]:
    '''
    Return list of positions for each mirror type.

    Parameters
    ----------
    - `mirror` (`MirrorType`): Mirror

    Returns
    -------
    - `List[int]`: List of valid positions
    '''
    match mirror:
        case MirrorType.M4:
            number_of_positions = 5
        case MirrorType.M8:
            number_of_positions = 6
        case _:
            number_of_positions = 3

    return list(range(1, number_of_positions+1))

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

        case MirrorType.M4:
            if position in [1, 2, 3]:
                return creator.create_au(str(position), vcm_size=VCMSize.Normal, without_mgc=True)

            else:
                return creator.create_au(str(position), mgc_size=MGCSize.Large, without_vcm=True)

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

        case _:
            return creator.create_au(str(position), MGCSize.Medium, VCMSize.Normal)

def create_all_au_models(version: int) -> List[HardwareModel]:
    '''
    Iterate through all mirrors and all positions and create AU models

    Parameters
    ----------
    - `version` (`int`): Version to create

    Returns
    -------
    - `List[HardwareModel]`: List of all hardware models linked together
    '''
    hardware_models = []
    for mirror in MirrorType:
        positions = valid_positions(mirror)
        for position in positions:
            hardware_models.extend(
                create_model(mirror, position, version)
            )

    return hardware_models

def main(version: int):
    # Create models from parameters
    au_models = create_all_au_models(version)

    # Connect to database
    au5k_db = AUProductionDB(ip_address='127.0.0.1', port_number=3306, username='root', password='Password123!')
    au5k_db.connect(database_name='production')

    # Create hardware_models table (if it doesn't already exist)
    ProductionBase.metadata.create_all(au5k_db.engine)

    for hardware_model in au_models:
        au5k_db.session.add(hardware_model)
        au5k_db.session.commit()

    au5k_db.disconnect()

if __name__ == '__main__':
    setup_logger()
    main(evaluate_args())
