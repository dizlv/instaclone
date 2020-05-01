from flask import Blueprint

from applications.photos import views

blueprint = Blueprint(
    name='photos',
    import_name=__name__,
    template_folder='templates',
)

blueprint.add_url_rule(
    rule='/upload_photo/',
    view_func=views.UploadPhotoView.as_view('upload-photo'),
)

blueprint.add_url_rule(
    rule='/photo/<photo_id>/',
    view_func=views.PhotoDetailView.as_view('photo-detail'),
)

blueprint.add_url_rule(
    rule='/uploads/<file_name>/',
    view_func=views.ViewFile.as_view('view-file'),
)
