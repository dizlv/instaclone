import time
import hashlib

import flask

from flask_login import current_user

from flask_wtf import FlaskForm

from flask_wtf.file import (
    FileField,
    FileRequired,
)

from extensions.database import db

from applications.photos import models


class PhotoForm(FlaskForm):
    photo = FileField(
        label='Select Photo',

        validators=[
            FileRequired(),
        ]
    )

    def generate_file_name(self, file_name, extension):
        # Generate new unique file name
        new_file_name = file_name + str(time.time())
        new_file_name = hashlib.sha256(new_file_name.encode('utf-8')).hexdigest()

        # Concatenate new file name and extension
        new_file_name = f'{new_file_name}.{extension}'

        return new_file_name

    def fs_store(self, photo_file, file_name):
        # Generate file system path for new file
        fs_path = flask.current_app.config['UPLOADS_DIRECTORY'] / file_name

        # Save file on fs
        photo_file.save(fs_path)

    def db_store(self, file_name, user_id):
        # Create photo model instance
        photo = models.Photo(
            path=file_name,
            user_id=user_id,
        )

        # Save into the database
        db.session.add(photo)
        db.session.commit()

        return photo

    def save(self):
        # Get original file object
        photo_file = self.photo.data

        # Get file name and extension
        file_name, extension = photo_file.filename.rsplit('.', 1)

        new_file_name = self.generate_file_name(
            file_name=file_name,
            extension=extension,
        )

        self.fs_store(
            photo_file=photo_file,
            file_name=new_file_name,
        )

        photo = self.db_store(
            file_name=new_file_name,
            user_id=current_user.id,
        )

        return photo
