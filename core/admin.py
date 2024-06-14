from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'level', 'country', 'type', 'feedback']
    list_filter = ['level', 'country', 'type', 'feedback']
    search_fields = ['company', 'position', 'country', 'type', 'feedback']



admin.site.register(Application, ApplicationAdmin)
