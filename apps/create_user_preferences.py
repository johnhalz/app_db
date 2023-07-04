'''Create user preferences in app database'''
import logging
from typing import List

from numpy import arange

from app_db.sql_models import UserPreference, UserPreferenceBase, AppLightingPreference, LanguagePreference
from app_db.interface import AUProductionDB

def setup_logger():
    '''Setup logger for app'''
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
        format='[%(asctime)s] %(levelname)-9s %(message)s'
    )

def create_user_preference(app_lighting_preference: AppLightingPreference,
                           language: LanguagePreference,
                           scanner_haptics: bool,
                           scanner_timeout: int) -> UserPreference:
    return UserPreference(app_lighting_preference, language, scanner_haptics, scanner_timeout)

def create_all_user_preferences() -> List[UserPreference]:
    '''
    Create all possible user preferences.

    Returns
    -------
    - `List[UserPreference]`: List of user preferences
    '''
    user_preferences = []
    for app_lighting_preference in AppLightingPreference:
        for language_preference in LanguagePreference:
            for timeout_preference in arange(start=5, stop=30, step=5):
                user_preferences.extend(
                    [
                        UserPreference(app_lighting_preference.value, language_preference.value, False, timeout_preference),
                        UserPreference(app_lighting_preference.value, language_preference.value, True, timeout_preference)
                    ]
                )

    return user_preferences

def main():
    # Create new users
    user_preferences = create_all_user_preferences()

    # Connect to database
    au5k_db = AUProductionDB(ip_address='127.0.0.1', port_number=3306, username='root', password='Password123!')
    au5k_db.connect(database_name='users')

    # Create users table (if it doesn't already exist)
    UserPreferenceBase.metadata.create_all(au5k_db.engine)

    for user_preference in user_preferences:
        au5k_db.session.add(user_preference)
        au5k_db.session.commit()

    au5k_db.disconnect()

if __name__ == '__main__':
    setup_logger()
    main()
