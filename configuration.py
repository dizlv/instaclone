import pathlib

SECRET_KEY = 'asdlkasdlkajsd'
SQLALCHEMY_DATABASE_URI = 'sqlite:///instaclone.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOADS_DIRECTORY = pathlib.Path(__file__).parent / 'uploads'
