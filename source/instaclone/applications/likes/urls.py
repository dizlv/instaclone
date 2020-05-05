from flask import Blueprint

from instaclone.applications.likes import views

blueprint = Blueprint(
    name='likes',
    import_name=__name__,
    template_folder='templates',
)

blueprint.add_url_rule(
    rule='/add_like/<photo_id>/',
    view_func=views.AddLikeView.as_view('add-like'),
)
