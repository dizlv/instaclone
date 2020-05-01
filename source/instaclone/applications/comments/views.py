import flask

from flask.views import MethodView

from flask_login import (
    login_required,
    current_user,
)

from instaclone.extensions.database import db

from instaclone.applications.photos.models import Photo


class AddCommentView(MethodView):
    decorators = [
        login_required,
    ]

    def post(self, photo_id):
        photo = Photo.query.get(photo_id)

        if photo is None:
            return 'Photo not found', 404

        comment = photo.add_comment(
            from_user=current_user,
            content=flask.request.form['content'],
        )

        db.session.add(comment)
        db.session.commit()

        return 'ok'
