import flask
from flask.views import MethodView

from werkzeug.security import generate_password_hash

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

        return hashed_password
