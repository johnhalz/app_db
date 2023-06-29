import logging
from typing import List
from random import randint, choice

from app_db.interface import AUProductionDB
from app_db.sql_models import Hardware, StockStatus, BuildStatus

def setup_logger():
    '''Setup logger for app'''
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
        format='[%(asctime)s] %(levelname)-9s %(message)s'
    )

def create_au() -> List[Hardware]:
    '''
    Create a single AU instance with partially complete parts
    '''
    hardware_list = []
    new_au = Hardware(
        order_number = randint(200000, 999999),
        serial_number = f'11-{randint(1000, 9999)}-{randint(1000, 9999)}',
        material_number = f'AU-M{randint(1, 9)}',
        parent_id = None,
        stock_status = 'Parts Available',
        build_status = 'Not Started',
        position = str(choice([10, 20, 30, 13, 23, 12])),
        version = "2"
    )

    new_vcm_1 = Hardware(
        order_number = randint(200000, new_au.order_number),
        serial_number = f'11-{randint(1000, 9999)}-{randint(1000, 9999)}',
        material_number = f"VCM-{choice(['N', 'L'])}",
        parent_id = new_au.id,
        stock_status = StockStatus.parts_available.name,
        build_status = BuildStatus.built.name,
        position = '1',
        version = '3.1'
    )

    new_vcm_2 = Hardware(
        order_number = randint(200000, new_au.order_number),
        serial_number = f'11-{randint(1000, 9999)}-{randint(1000, 9999)}',
        material_number = new_vcm_1.material_number,
        parent_id = new_au.id,
        stock_status = StockStatus.parts_available.name,
        build_status = BuildStatus.building.name,
        position = '2',
        version = '3.1'
    )

    new_mgc = Hardware(
        order_number = randint(200000, new_au.order_number),
        serial_number = f'11-{randint(1000, 9999)}-{randint(1000, 9999)}',
        material_number = f"MGC-{choice(['N', 'L'])}",
    )

def main(number_of_aus_to_create: int = 5):
    pass

if __name__ == '__main__':
    setup_logger()
    main()
