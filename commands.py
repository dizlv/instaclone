from application import application
from extensions.database import db


@application.cli.command()
def create_database():
    db.create_all()
