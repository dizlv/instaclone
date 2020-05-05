import flask

from flask.views import MethodView

from flask_login import login_required

from instaclone.applications.photos.models import Photo
from instaclone.applications.views import FormViewMixin
from instaclone.applications.photos import forms


class UploadPhotoView(MethodView, FormViewMixin):
    form_class = forms.PhotoForm
    template_name = 'photos/upload_photo.html'

    decorators = [
        login_required,
    ]

    def post(self):
        form = self.get_form()

        if form.validate_on_submit():
            photo = form.save()

            photo_link = photo.photo_link()
            response = flask.redirect(location=photo_link)

            return response

        return flask.render_template(
            template_name_or_list=self.get_template_name(),
            form=form,
        )


class ViewFile(MethodView):
    def get(self, file_name):
        uploads_directory = str(flask.current_app.config['UPLOADS_DIRECTORY'])

        return flask.send_from_directory(uploads_directory, file_name)


class PhotoDetailView(MethodView):
    def get(self, photo_id):
        photo = Photo.query.get(photo_id)

        if photo is None:
            return 'Photo not found', 404

        return flask.render_template(
            template_name_or_list='photos/photo_detail.html',
            photo=photo,
        )
