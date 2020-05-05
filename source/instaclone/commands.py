from instaclone.application import application
from instaclone.extensions.database import db


@application.cli.command()
def create_database():
    db.create_all()
