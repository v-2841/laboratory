from django.contrib import admin

from reagents.models import Reagent


class ReagentAdmin(admin.ModelAdmin):
    list_display = ['index', 'name', 'grade', 'amount',
                    'manufacture_date', 'expiration_date']
    search_fields = ['name']


admin.site.register(Reagent, ReagentAdmin)
