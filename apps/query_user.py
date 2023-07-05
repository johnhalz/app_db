'''Query User Example'''
import logging

from app_db.interface import AUProductionDB
from app_db.sql_models import User, UserPreference

def setup_logger():
    '''Setup logger for app'''
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
        format='[%(asctime)s] %(levelname)-9s %(message)s'
    )

def main():
    # Connect to database
    au5k_db = AUProductionDB(ip_address='127.0.0.1', port_number=3306, username='root', password='Password123!')
    au5k_db.connect(database_name='users')

    user = au5k_db.session.query(User).first()
    print(user.__dict__)

    user_pref: UserPreference = user.user_preference
    print(user_pref.__dict__)

    au5k_db.disconnect()
    pass

if __name__ == '__main__':
    setup_logger()
    main()