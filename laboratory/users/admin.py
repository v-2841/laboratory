from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.models import Invitation, User


class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name',
                    'laboratory_staff', 'is_superuser']
    fieldsets = (
        (None, {
            'fields': ('username', 'password')}),
        ('Персональные данные', {
            'fields': ('first_name', 'last_name', 'email')}),
        ('Права пользователя', {
            'fields': ('is_active', 'laboratory_staff', 'is_staff',
                       'is_superuser')}),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')}),
    )


class InvitationAdmin(admin.ModelAdmin):
    list_display = ['email', 'sender', 'is_used']
    search_fields = ['email', 'sender__username']


admin.site.register(User, UserAdmin)
admin.site.register(Invitation, InvitationAdmin)
admin.site.unregister(Group)
