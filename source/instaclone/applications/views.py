import flask


class FormViewMixin:
    form_class = None
    template_name = None

    def get_form_class(self):
        return self.form_class

    def get_form(self):
        form_class = self.get_form_class()

        form = form_class()

        return form

    def get_template_name(self):
        return self.template_name

    def get(self):
        form = self.get_form()
        template_name = self.get_template_name()

        return flask.render_template(
            template_name_or_list=template_name,
            form=form,
        )
