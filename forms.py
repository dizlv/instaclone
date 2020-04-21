from flask_wtf import FlaskForm

from flask_login import login_user

from wtforms import (
    StringField,
    PasswordField,
)

from wtforms.validators import (
    Email,
    DataRequired,
    EqualTo,
)

from database import db

import models
import exceptions


class RegistrationForm(FlaskForm):
    email = StringField(
        label='Email Address',

        validators=[
            Email(),
        ],
    )

    password = PasswordField(
        label='New Password',

        validators=[
            DataRequired(),

            EqualTo(
                fieldname='confirm',
                message='Passwords must match',
            ),
        ],
    )

    confirm = PasswordField(
        label='Repeat Password',

        validators=[
            DataRequired(),
        ],
    )

    def save(self):
        user = models.User.create(
            email=self.email.data,
            password=self.password.data,
        )

        db.session.add(user)
        db.session.commit()


class LoginForm(FlaskForm):
    email = StringField(
        label='Email Address',

        validators=[
            Email(),
        ],
    )

    password = PasswordField(
        label='Enter Password',

        validators=[
            DataRequired(),
        ],
    )

    def login(self):
        user = models.User.query.filter_by(email=self.email.data).first()

        if user is None:
            raise exceptions.LoginException('Such user not found')

        password_match = user.check_password(password=self.password.data)

        if password_match:
            login_user(user)

        else:
            raise exceptions.LoginException('Wrong credentials')
