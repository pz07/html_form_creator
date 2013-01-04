from creator.models import HtmlFormTemplate, HtmlField, HtmlForm, HtmlFieldValue
from django.contrib import admin

class HtmlFieldInline(admin.TabularInline):
    model = HtmlField
    extra = 3

class HtmlFormTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'default_action', 'default_method', 'created_at')
    list_filter = ['author']
    search_fields = ['name']

    inlines = [HtmlFieldInline]

admin.site.register(HtmlFormTemplate, HtmlFormTemplateAdmin)
admin.site.register(HtmlField)
admin.site.register(HtmlForm)
admin.site.register(HtmlFieldValue)
