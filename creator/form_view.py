__author__ = 'pawel'

from models import HtmlField

class FormView:

    def __init__(self, html_template, html_form):
        self.html_form = html_form
        self.html_template = html_template

    def method(self):
        return self.html_form.method

    def action(self):
        return self.html_form.action

    def fields(self):
        #TODO lazy initialize
        html_fields = HtmlField.objects.filter(html_form_template_id=self.html_template.id)

        fields = []
        for html_field in html_fields:
            fields.append(FieldView(html_field))

        return fields

class FieldView:

    def __init__(self, html_field):
        self.html_field = html_field

    def type(self):
        return self.html_field.field_type

    def name(self):
        return self.html_field.name
