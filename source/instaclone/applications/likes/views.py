from flask.views import MethodView

from flask_login import (
    login_required,
    current_user,
)

from werkzeug.exceptions import BadRequest

from instaclone.extensions.database import db
from instaclone.applications.photos.models import Photo
from instaclone.exceptions import CoreException


class AddLikeView(MethodView):
    decorators = [
        login_required,
    ]

    def post(self, photo_id):
        photo = Photo.query.get(photo_id)

        if photo is None:
            return 'Photo not found', 404

        try:
            like = photo.add_like(from_user=current_user)

        except CoreException as exception:
            raise BadRequest(description=str(exception)) from exception

        db.session.add(like)
        db.session.commit()

        return 'ok'
