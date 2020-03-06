import flask

from views import UserView


def create_application():
    application = flask.Flask(__name__)

    application.config.from_pyfile('configuration.py')

    from database import db

    db.init_app(app=application)

    return application


application = create_application()


@application.cli.command()
def create_database():
    from database import db

    db.create_all()


application.add_url_rule(
    rule='/registration/',
    view_func=UserView.as_view('registration'),
)

application.run()
