from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import HtmlFormTemplate, HtmlForm

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

    return render_to_response('form.html', {'templates': templates, 'template': template, 'forms': forms, 'form': form})
