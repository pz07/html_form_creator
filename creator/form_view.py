__author__ = 'pawel'

from models import HtmlField, HtmlFieldValue

class FormView:

    def __init__(self, html_template, html_form):
        self.html_form = html_form
        self.html_template = html_template

    def id(self):
        return self.html_form.id

    def method(self):
        return self.html_form.method

    def action(self):
        return self.html_form.action

    def fields(self):
        #TODO lazy initialize
        html_fields = HtmlField.objects.filter(html_form_template_id=self.html_template.id)

        html_field_values = HtmlFieldValue.objects.filter(html_form=self.html_form)
        html_field_values_dict = dict([(x.html_field_id,x) for x in html_field_values])

        print "TUTUTUT"
        print html_field_values_dict

        fields = []
        for html_field in html_fields:
            fields.append(FieldView(html_field, html_field_values_dict.get(html_field.id)))

        return fields

class FieldView:

    def __init__(self, html_field, html_field_value = None):
        self.html_field = html_field
        self.html_field_value = html_field_value

        self.value_processors = []
        self.value_processors.append(VariableProcessor())
        self.value_processors.append(PatternProcessor())

    def id(self):
        return self.html_field.id

    def type(self):
        return self.html_field.field_type

    def name(self):
        return self.html_field.name

    def default_value(self):
        if self.html_field_value and self.html_field_value.default_value:
            return self.html_field_value.default_value
        else:
            return self.html_field.default_value

    def template_value(self):
        return self.html_field.default_value

    def value(self):
        #TODO value z sesji, value z html_field_value
        value = self.html_field.default_value
        if self.html_field_value and self.html_field_value.default_value:
            value = self.html_field_value.default_value

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