'''Connection to MariaDB interface'''
import argparse
import logging

from app_db.interface import AUProductionDB
from app_db.sql_models import (
    HardwareBase,
    NonComplianceBase,
    ProductionStepBase,
    SpecificationBase,
    UserPreferenceBase,
    UserBase,
    MeasurementBase,
    ResultBase,
    EquipmentBase,
    HardwareModelBase
)

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
        prog='Create Tables',
        description="Connect and create all known tables to MariaDB (if they don't exist)"
    )
    parser.add_argument('--address',
                        dest='ip_address',
                        type=str,
                        required=False,
                        default='127.0.0.1',
                        help='IP address of database')
    parser.add_argument('-p', '--port',
                        dest='port_number',
                        type=int,
                        default=3306,
                        help='Port number of database')
    parser.add_argument('--username',
                        dest='username',
                        type=str,
                        default='root',
                        help='Username to access database')
    parser.add_argument('--password',
                        dest='password',
                        type=str,
                        default='Password123!',
                        help='Password to access database')

    return parser.parse_args()

def evaluate_args():
    '''Evaluate input arguments'''
    args = parse_arguments()
    return args.ip_address, args.port_number, args.username, args.password

def main(ip_address: str, port_number: int, username: str, password: str):
    production_db = AUProductionDB(ip_address, port_number, username, password)
    production_db.connect(database_name='production')

    bases = [ResultBase, HardwareBase, NonComplianceBase, ProductionStepBase, ResultBase, HardwareModelBase,
             SpecificationBase, UserPreferenceBase, UserBase, MeasurementBase, EquipmentBase]
    for base in bases:
        base.metadata.create_all(production_db.engine)

    logging.info('All tables created!')

    production_db.disconnect()

if __name__ == '__main__':
    setup_logger()
    main(*evaluate_args())
