from flask import url_for

from database import db
from exceptions import CoreException


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

    likes = db.relationship(
        'Like',
        backref='photo',
        lazy=True,
    )

    comments = db.relationship(
        'Comment',
        backref='photo',
        lazy=True,
    )

    def photo_link(self):
        link = url_for(
            endpoint='view-file',
            file_name=self.path,
        )

        return link

    def like_link(self):
        link = url_for(
            endpoint='add-like',
            photo_id=self.id,
        )

        return link

    def comment_link(self):
        link = url_for(
            endpoint='add-comment',
            photo_id=self.id,
        )

        return link

    def add_like(self, from_user):
        already_liked = Like.query.filter(
            Like.user_id == from_user.id,
            Like.photo_id == self.id,
        ).count()

        if already_liked:
            raise CoreException('Sorry, we can not accept your like more than once!')

        like = Like(
            user_id=from_user.id,
            photo_id=self.id,
        )

        return like

    def add_comment(self, from_user, content):
        comment = Comment(
            user_id=from_user.id,
            photo_id=self.id,
            content=content,
        )

        return comment


class Like(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
    )

    photo_id = db.Column(
        db.Integer,
        db.ForeignKey('photo.id'),
        nullable=False,
    )


class Comment(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
    )

    photo_id = db.Column(
        db.Integer,
        db.ForeignKey('photo.id'),
        nullable=False,
    )

    content = db.Column(
        db.String,
        nullable=False,
    )
