from django.contrib import admin

from results.models import Result


class ResultAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ['pub_date', 'sample_name', 'analysis_name', 'standard',
                    'measurement_unit', 'result', 'researcher', 'is_processed']
    search_fields = ['sample_name', 'analysis_name']
    fieldsets = (
        ('Образец', {
            'fields': ('sample_name',)}),
        ('Исследование', {
            'fields': ('analysis_name', 'standard', 'measurement_unit',
                       'result', 'researcher')}),
        ('Обработка', {
            'fields': ('is_processed',)}),
    )


admin.site.register(Result, ResultAdmin)
