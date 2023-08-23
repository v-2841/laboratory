from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import Group

from users.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'is_staff',)
    ordering = ('last_name', 'first_name',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password')}),
        ('Персональные данные', {
            'fields': ('first_name', 'last_name', 'email')}),
        ('Права пользователя', {
            'fields': ('is_active', 'is_staff',
                       'is_superuser', 'groups')}),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)
