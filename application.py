import flask

from views import (
    UserProfileView,
    UserRegistrationView,
    UserLoginView,
    UploadPhotoView,
    ViewFile,
    AddLikeView,
)


def create_application():
    application = flask.Flask(__name__)

    application.config.from_pyfile('configuration.py')

    from database import db

    db.init_app(app=application)

    from auth import login_manager

    login_manager.init_app(app=application)

    return application


application = create_application()


@application.cli.command()
def create_database():
    from database import db

    db.create_all()


application.add_url_rule(
    rule='/registration/',
    view_func=UserRegistrationView.as_view('registration'),
)

application.add_url_rule(
    rule='/login/',
    view_func=UserLoginView.as_view('login'),
)

application.add_url_rule(
    rule='/upload_photo/',
    view_func=UploadPhotoView.as_view('upload-photo'),
)

application.add_url_rule(
    rule='/add_like/<photo_id>/',
    view_func=AddLikeView.as_view('add-like'),
)

application.add_url_rule(
    rule='/uploads/<file_name>/',
    view_func=ViewFile.as_view('view-file'),
)

application.add_url_rule(
    rule='/user/<user_id>/',
    view_func=UserProfileView.as_view('user-profile'),
)

application.run()
