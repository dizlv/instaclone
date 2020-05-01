from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

from extensions.database import db


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

    likes = db.relationship(
        'Like',
        backref='user',
        lazy=True,
    )

    comments = db.relationship(
        'Comment',
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

    def set_password(self, password):
        self.password = generate_password_hash(password=password)

    def check_password(self, password):
        is_correct = check_password_hash(
            pwhash=self.password,
            password=password,
        )

        return is_correct

    @classmethod
    def create(cls, email, password):
        instance = cls(
            email=email,
        )

        instance.set_password(password=password)

        return instance
