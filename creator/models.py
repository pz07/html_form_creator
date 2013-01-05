from django.db import models
from datetime import datetime

class HtmlFormTemplate(models.Model):
    METHOD_CHOICES = (
        ('POST', 'POST'),
        ('GET', 'GET')
    )

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField('created at', default=datetime.now)
    default_action = models.URLField(blank = True)
    default_method = models.CharField(max_length=4, choices = METHOD_CHOICES)

    def __unicode__(self):
        return "HtmlFormTemplate#"+self.name

class HtmlField(models.Model):
    FIELD_TYPE_CHOICES = (
        ('text', 'text'),
        ('select', 'select')
    )

    html_form_template = models.ForeignKey(HtmlFormTemplate)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024, blank = True)
    field_type = models.CharField(max_length=32, choices = FIELD_TYPE_CHOICES)
    default_value = models.CharField(max_length=255, blank = True)
    size = models.IntegerField(null = True, blank = True)

    def __unicode__(self):
        return "HtmlField#"+self.name

class HtmlForm(models.Model):
    METHOD_CHOICES = (
        ('POST', 'POST'),
        ('GET', 'GET')
    )

    html_form_template = models.ForeignKey(HtmlFormTemplate)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField('created at', default=datetime.now)
    action = models.URLField()
    method = models.CharField(max_length=4, choices = METHOD_CHOICES)

    def __unicode__(self):
        return "HtmlForm#"+self.name

class HtmlFieldValue(models.Model):
    html_form = models.ForeignKey(HtmlForm)
    html_field = models.ForeignKey(HtmlField)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return "HtmlFieldValue#"+self.value

