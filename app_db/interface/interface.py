import logging
from typing import List, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from .utils import ip_is_valid, port_is_valid, ip_is_reachable

class AUProductionDB:
    def __init__(self, ip_address: str, port_number: int,
                 username: str, password: str, timeout: int = 10) -> None:
        # Verify that input address is valid
        if not ip_is_valid(ip_address):
            raise ValueError(
                f'Input IP address {ip_address} is not valid.'
            )

        # Verify that input port number is valid
        if not port_is_valid(port_number):
            raise ValueError(
                f'Input port number {port_number} is not valid.'
            )

        # Assign member variables
        self.ip_address = ip_address
        self.port_number = port_number
        self.password = password
        self.timeout = timeout
        self.username = username
        self.password = password

        self.session = None
        self.engine = None

    def connect(self, database_name: str = None):
        '''Connect to database'''
        if database_name is None:
            raise ValueError('You need to provide a database name!')

        if not ip_is_reachable(self.ip_address, self.port_number, timeout=self.timeout):
            raise ConnectionError(
                f'Unable to reach the address {self.ip_address}:{self.port_number}.'
            )

        if not self.connected:
            self.engine = create_engine(
                f'mysql+pymysql://{self.username}:{self.password}@{self.ip_address}:{self.port_number}/{database_name}',
                pool_timeout=float(self.timeout)
            )

            self.session = sessionmaker(bind=self.engine)()
            logging.info(f'Successfully connected to {self.engine.url}')

    def disconnect(self):
        if self.connected:
            self.session.close()
            self.engine.dispose()
            logging.info(f'Successfully disconnected from {self.engine.url}')

        self.session = None
        self.engine = None

    def read_table_to_df(self, table_name: str) -> pd.DataFrame:
        try:
            return pd.read_sql_table(table_name=table_name, con=self.engine)
        except Exception as e:
            raise LookupError(f'Unable to read data from {table_name}.')

    def read_table_to_model(self, model: Any) -> List[Any]:
        return self.session.query(model).all()

    @property
    def connected(self) -> bool:
        if self.session is None:
            return False

        return self.session.is_active
