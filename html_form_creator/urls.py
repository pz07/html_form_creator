from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^html_form_creator/', include('html_form_creator.foo.urls')),

    url(r'^html_form_creator/$', 'creator.views.templates', name='templates'),
    url(r'^html_form_creator/template/(?P<template_id>\d+)/forms$', 'creator.views.template'),
    url(r'^html_form_creator/template/(?P<template_id>\d+)/form/(?P<form_id>\d+)/form$', 'creator.views.form'),
    url(r'^html_form_creator/template/(?P<template_id>\d+)/form/(?P<form_id>\d+)/edit$', 'creator.views.form_edit'),

    url(r'^html_form_creator/admin/', include(admin.site.urls)),
)
