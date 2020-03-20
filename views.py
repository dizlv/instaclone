import flask

from flask.views import MethodView

from flask_login import (
    login_user,
)


from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

from database import db
from models import User


def create_user(email, hashed_password):
    user = User(
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()


class UserView(MethodView):
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

