from django.contrib import admin

from laboratories.models import Laboratory


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_full_name']

    @admin.display(description='Администратор лаборатории')
    def admin_full_name(self, obj):
        return f'{obj.admin.last_name} {obj.admin.first_name}'


admin.site.register(Laboratory, LaboratoryAdmin)
