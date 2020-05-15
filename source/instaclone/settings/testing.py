from instaclone.settings.core import *

TESTING = True
WTF_CSRF_ENABLED = False

SQLALCHEMY_DATABASE_URI = f'sqlite:///{ROOT_DIRECTORY}/instaclone_testing.db'
