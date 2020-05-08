import flask
from flask.views import MethodView


class AboutView(MethodView):
    def get(self):
        return flask.render_template(
            template_name_or_list='core/about.html'
        )
