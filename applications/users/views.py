import flask

from flask.views import MethodView

from exceptions import LoginException

from applications.users import forms
from applications.users.models import User
from applications.views import FormViewMixin


class UserRegistrationView(MethodView, FormViewMixin):
    form_class = forms.RegistrationForm
    template_name = 'users/registration.html'

    def post(self):
        form = self.get_form()

        if form.validate_on_submit():
            form.save()

        return flask.render_template(
            template_name_or_list=self.get_template_name(),
            form=form,
        )


class UserLoginView(MethodView, FormViewMixin):
    form_class = forms.LoginForm
    template_name = 'users/login.html'

    def post(self):
        form = self.get_form()

        if form.validate_on_submit():
            try:
                form.login()

            except LoginException as exception:
                flask.flash(message=str(exception))

        return flask.render_template(
            template_name_or_list=self.get_template_name(),
            form=form,
        )


class UserProfileView(MethodView):
    def get(self, user_id):
        user = User.query.get(user_id)

        if user is None:
            return 'User not found!', 404

        return flask.render_template(
            template_name_or_list='users/profile_photos.html',
            photos=user.photos,
        )
