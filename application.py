import hashlib
import flask

secret_key = 'nehro356ateniggjoe356hipie'

application = flask.Flask(__name__)


@application.route('/registration/', methods=['GET', 'POST'])
def registration():
    if flask.request.method == 'POST':
        password = flask.request.form['password'] + secret_key

        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))

        hashed_password = hasher.hexdigest()

        return hashed_password
    return flask.render_template('registration.html')


application.run()
