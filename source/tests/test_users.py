import pytest

from flask import url_for

from instaclone.application import create_application
from instaclone.applications.users.models import User
from instaclone.extensions.database import db


@pytest.fixture
def app():
    application = create_application(configuration='settings/testing.py')

    return application


@pytest.fixture
def db_session(app):
    with app.app_context():
        db.create_all()

        yield db

        db.drop_all()


def test_registration(client, db_session):
    registration_link = url_for(
        endpoint='users.registration',
    )

    email = 'test@gmail.com'
    password = 'test'

    response = client.post(
        registration_link,

        data={
            'email': email,
            'password': password,
            'confirm': password,
        },
    )

    assert response.status_code == 200

    user = User.query.filter_by(email=email).first()

    assert user is not None


def test_non_existing_profile(client, db_session):
    profile_link = url_for(
        endpoint='users.user-profile',
        user_id=9999999999,
    )

    response = client.get(profile_link)

    assert response.status_code == 404
