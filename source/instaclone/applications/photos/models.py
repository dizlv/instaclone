from flask import url_for

from instaclone.extensions.database import db
from instaclone.exceptions import CoreException

from instaclone.applications.likes.models import Like
from instaclone.applications.comments.models import Comment


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
            endpoint='photos.view-file',
            file_name=self.path,
        )

        return link

    def like_link(self):
        link = url_for(
            endpoint='likes.add-like',
            photo_id=self.id,
        )

        return link

    def comment_link(self):
        link = url_for(
            endpoint='comments.add-comment',
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
