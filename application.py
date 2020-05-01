import flask


class Application(flask.Flask):
    def load_configuration(self):
        self.config.from_pyfile('configuration.py')

    def configure_database(self):
        from extensions.database import db

        db.init_app(app=self)

    def configure_login_manager(self):
        from extensions.auth import login_manager

        login_manager.init_app(app=self)

    def register_applications(self):
        from applications.users.urls import blueprint as users_blueprint
        from applications.photos.urls import blueprint as photos_blueprint
        from applications.likes.urls import blueprint as likes_blueprint
        from applications.comments.urls import blueprint as comments_blueprint

        self.register_blueprint(blueprint=users_blueprint)
        self.register_blueprint(blueprint=photos_blueprint)
        self.register_blueprint(blueprint=likes_blueprint)
        self.register_blueprint(blueprint=comments_blueprint)

    @classmethod
    def create(cls):
        instance = cls(__name__)

        instance.load_configuration()
        instance.configure_database()
        instance.configure_login_manager()
        instance.register_applications()

        return instance


application = Application.create()

application.run()
