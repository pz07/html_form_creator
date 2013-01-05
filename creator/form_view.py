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

        self.value_processors = []
        self.value_processors.append(VariableProcessor())
        self.value_processors.append(PatternProcessor())

    def type(self):
        return self.html_field.field_type

    def name(self):
        return self.html_field.name

    def value(self):
        #TODO value z sesji, value z html_field_value
        value = self.html_field.default_value

        for processor in self.value_processors:
            value = processor.process(value)

        return value

    def size(self):
        if self.html_field.size:
            return self.html_field.size
        else:
            return "50"

class VariableProcessor:

    def process(self, value):
        import time
        import re

        value = re.sub(r'\$\{timestamp_as_long\}', str(int(time.time())), value)
        return value

class PatternProcessor:

    def process(self, value):
        if value.startswith("pattern:"):
            pattern = value.replace("pattern:", "", 1)

            import rstr
            gen_value = rstr.xeger(pattern)

            return gen_value
        else:
            return value