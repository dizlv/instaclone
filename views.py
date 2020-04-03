import time
import hashlib

import flask

from flask.views import MethodView

from flask_login import (
    login_user,
    login_required,
    current_user,
)


from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

from werkzeug.utils import secure_filename

from database import db

from models import (
    User,
    Photo,
)


def create_user(email, hashed_password):
    user = User(
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()


class UserRegistrationView(MethodView):
    def get(self):
        return flask.render_template('registration.html')

    def post(self):
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')

        hashed_password = generate_password_hash(password=password)

        create_user(
            email=email,
            hashed_password=hashed_password,
        )

        return 'Registration completed'


class UserLoginView(MethodView):
    def get(self):
        return flask.render_template('login.html')

    def post(self):
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user is None:
            return 'Such user not found'

        is_correct = check_password_hash(
            pwhash=user.password,
            password=password,
        )

        if is_correct:
            login_user(user=user)

            return 'Logged in successfully'

        return 'Wrong Credentials'


class UploadPhotoView(MethodView):
    decorators = [
        login_required,
    ]

    def get(self):
        return flask.render_template('upload_photo.html')

    def post(self):
        photo_file = flask.request.files['photo']

        file_name_parts = photo_file.filename.split('.')
        extension = file_name_parts[-1]

        secure_original_file_name = secure_filename(photo_file.filename) + str(time.time())
        secure_original_file_name = hashlib.sha256(secure_original_file_name.encode('utf-8')).hexdigest()

        file_name = flask.current_app.config['UPLOADS_DIRECTORY'] / secure_original_file_name

        photo_file.save(f'{file_name}.{extension}')

        photo = Photo(
            path=f'{secure_original_file_name}.{extension}',
            user_id=current_user.id,
        )

        db.session.add(photo)
        db.session.commit()

        photo_link = photo.photo_link()
        response = flask.redirect(location=photo_link)

        return response


class ViewFile(MethodView):
    def get(self, file_name):
        uploads_directory = str(flask.current_app.config['UPLOADS_DIRECTORY'])

        return flask.send_from_directory(uploads_directory, file_name)


class UserProfileView(MethodView):
    def get(self, user_id):
        user = User.query.get(user_id)

        if user is None:
            return 'User not found!', 404

        return flask.render_template(
            template_name_or_list='profile_photos.html',
            photos=user.photos,
        )
