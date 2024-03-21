from django.contrib import admin

from documents.models import Document


class DocumentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'standard']


admin.site.register(Document, DocumentAdmin)
