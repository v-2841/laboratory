from django.contrib import admin

from reagents.models import Reagent, ReagentName


class ReagentAdmin(admin.ModelAdmin):
    list_display = ['index', 'name', 'grade', 'expiration_date']
    search_fields = ['name__name']


class ReagentNameAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Reagent, ReagentAdmin)
admin.site.register(ReagentName, ReagentNameAdmin)
