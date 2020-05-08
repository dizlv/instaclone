from flask import Blueprint

from instaclone.applications.core import views

blueprint = Blueprint(
    name='core',
    import_name=__name__,
    template_folder='templates',
)

blueprint.add_url_rule(
    rule='/about/',
    view_func=views.AboutView.as_view('about'),
)
