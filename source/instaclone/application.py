import flask


class Application(flask.Flask):
    def load_configuration(self, configuration):
        self.config.from_pyfile(configuration)

    def configure_database(self):
        from instaclone.extensions.database import db

        db.init_app(app=self)

    def configure_login_manager(self):
        from instaclone.extensions.auth import login_manager

        login_manager.init_app(app=self)

    def register_applications(self):
        from instaclone.applications.users.urls import blueprint as users_blueprint
        from instaclone.applications.photos.urls import blueprint as photos_blueprint
        from instaclone.applications.likes.urls import blueprint as likes_blueprint
        from instaclone.applications.comments.urls import blueprint as comments_blueprint
        from instaclone.applications.core.urls import blueprint as core_blueprint

        self.register_blueprint(blueprint=users_blueprint)
        self.register_blueprint(blueprint=photos_blueprint)
        self.register_blueprint(blueprint=likes_blueprint)
        self.register_blueprint(blueprint=comments_blueprint)
        self.register_blueprint(blueprint=core_blueprint)


def create_application(configuration):
    instance = Application(__name__)

    instance.load_configuration(configuration=configuration)
    instance.configure_database()
    instance.configure_login_manager()
    instance.register_applications()

    return instance
