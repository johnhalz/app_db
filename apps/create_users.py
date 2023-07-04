'''Create user in App database'''
import argparse
import logging
import string
import random
from uuid import uuid4

from names import get_first_name, get_last_name
from passlib import pwd
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode

from app_db.sql_models import User, UserBase, UserRole
from app_db.interface import AUProductionDB

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
        prog='Create Users',
        description='App to create random users in app database'
    )
    parser.add_argument('-n', '--number',
                        dest='number_of_users',
                        type=int,
                        default=20,
                        help='Number of fake users to create')

    return parser.parse_args()

def evaluate_args():
    '''Evaluate input arguments'''
    args = parse_arguments()

    # Verify that input number is larger than 1
    if args.number_of_users < 1:
        raise ValueError('Number of users must be larger than 1.')

    return args.number_of_users

def encrypt_string(key: str, input_str: str) -> str:

    uuid_key = key.replace('-', '')
    cipher_suite = Fernet(urlsafe_b64encode(uuid_key.encode()))
    return cipher_suite.encrypt(input_str.encode()).decode()

def main(number_of_users: int):
    # Create new users
    new_users = []
    password_characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(number_of_users):
        user_id = uuid4()
        unenc_password = pwd.genword(length=8, chars=password_characters)

        new_users.append(
            User(
                id=user_id,
                first_name=get_first_name(),
                last_name=get_last_name(),
                encrpyted_password=encrypt_string(key=str(user_id), input_str=unenc_password),
                role=random.choice(list(UserRole)).value,
                user_preference_id=uuid4()
            )
        )

    # Connect to database
    au5k_db = AUProductionDB(ip_address='127.0.0.1', port_number=3306, username='root', password='Password123!')
    au5k_db.connect(database_name='users')

    # Create users table (if it doesn't already exist)
    UserBase.metadata.create_all(au5k_db.engine)

    for new_user in new_users:
        au5k_db.session.add(new_user)
        au5k_db.session.commit()

    au5k_db.disconnect()


if __name__ == '__main__':
    setup_logger()
    main(evaluate_args())
