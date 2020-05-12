import pathlib

SQLALCHEMY_TRACK_MODIFICATIONS = False

ROOT_DIRECTORY = pathlib.Path(__file__).parent.parent.parent.parent
UPLOADS_DIRECTORY = ROOT_DIRECTORY / 'uploads'
