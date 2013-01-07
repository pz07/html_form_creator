from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from creator.models import HtmlFieldValue

from models import HtmlFormTemplate, HtmlForm, HtmlField

from form_view import FormView

from django.core.urlresolvers import reverse

def templates(request):
    templates = HtmlFormTemplate.objects.all().order_by('-name')
    return render_to_response('template_list.html', {'templates': templates})

def template(request, template_id):
    #TODO do sesji?
    templates = HtmlFormTemplate.objects.all().order_by('-name')
    template = HtmlFormTemplate.objects.get(pk=template_id)

    forms = HtmlForm.objects.filter(html_form_template=template)

    return render_to_response('template_forms.html', {'templates': templates, 'template': template, 'forms': forms})

def form(request, template_id, form_id):
    #TODO do sesji?
    templates = HtmlFormTemplate.objects.all().order_by('-name')
    template = HtmlFormTemplate.objects.get(pk=template_id)

    forms = HtmlForm.objects.filter(html_form_template=template)
    form = HtmlForm.objects.get(pk=form_id)

    form_view = FormView(template, form)

    return render_to_response('form.html', {'templates': templates, 'template': template, 'forms': forms, 'form_view': form_view})

def form_edit(request, template_id, form_id):
    #TODO do sesji?
    templates = HtmlFormTemplate.objects.all().order_by('-name')
    template = HtmlFormTemplate.objects.get(pk=template_id)

    forms = HtmlForm.objects.filter(html_form_template=template)
    form = HtmlForm.objects.get(pk=form_id)

    form_view = FormView(template, form)

    if request.method == 'POST':
        form.action = request.POST.get("form_action", '')
        form.method = request.POST.get("form_method", '')

        form.save()

        for field in form_view.fields():

            import logging
            logger = logging.getLogger(__name__)

            new_field_value = request.POST.get("field_{0}_value".format(field.id()), None)

            if new_field_value != field.default_value() and new_field_value:
                try:
                    field_to_update = HtmlFieldValue.objects.get(html_field_id=field.id, html_form=form)
                except ObjectDoesNotExist:
                    field_to_update = HtmlFieldValue(html_form=form, html_field=HtmlField.objects.get(pk=field.id))

                field_to_update.default_value = new_field_value
                field_to_update.save()
            elif new_field_value == field.template_value():
                field_to_update = None
                try:
                    field_to_update = HtmlFieldValue.objects.get(html_field_id=field.id, html_form=form)
                except ObjectDoesNotExist:
                    pass

                if field_to_update:
                    field_to_update.delete()

        return redirect(reverse('creator.views.form', args=(template.id, form.id,)))
    else:
        return render_to_response('form_edit.html', {'templates': templates, 'template': template, 'forms': forms, 'form_view': form_view})
