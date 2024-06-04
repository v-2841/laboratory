from django.contrib import admin
from django.contrib.admin.models import LogEntry

from laboratories.models import Laboratory


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'


admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
