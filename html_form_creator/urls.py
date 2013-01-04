from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'html_form_creator.views.home', name='home'),
    # url(r'^html_form_creator/', include('html_form_creator.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
