from flask import Blueprint

from applications.users import views

blueprint = Blueprint(
    name='users',
    import_name=__name__,
    template_folder='templates',
)

blueprint.add_url_rule(
    rule='/registration/',
    view_func=views.UserRegistrationView.as_view('registration'),
)

blueprint.add_url_rule(
    rule='/login/',
    view_func=views.UserLoginView.as_view('login'),
)

blueprint.add_url_rule(
    rule='/user/<user_id>/',
    view_func=views.UserProfileView.as_view('user-profile'),
)
