import os

from instaclone.application import create_application
from instaclone.extensions.database import db

configuration = os.environ['APPLICATION_CONFIG_FILE']

application = create_application(configuration=configuration)

try:
    db.create_all(app=application)

except:
    pass
