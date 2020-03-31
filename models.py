from flask import url_for

from database import db


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.String(80),
        unique=True,
        nullable=False,
    )

    password = db.Column(
        db.String(200),
        nullable=False,
    )

    photos = db.relationship(
        'Photo',
        backref='user',
        lazy=True,
    )

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Photo(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    path = db.Column(
        db.String,
        unique=True,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
    )

    def photo_link(self):
        link = url_for(
            endpoint='view-file',
            file_name=self.path,
        )

        return link
