from flask import Blueprint

from instaclone.applications.comments import views

blueprint = Blueprint(
    name='comments',
    import_name=__name__,
    template_folder='templates',
)

blueprint.add_url_rule(
    rule='/add_comment/<photo_id>/',
    view_func=views.AddCommentView.as_view('add-comment'),
)
