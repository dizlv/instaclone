import hashlib
import flask

secret_key = '01'


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


@application.route('/registration/', methods=['GET', 'POST'])
def registration():
    if flask.request.method == 'GET':
        return flask.render_template('registration.html')

    email = flask.request.form.get('email')
    password = flask.request.form.get('password') + secret_key

    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))

    hashed_password = hasher.hexdigest()

    return hashed_password


application.run()
