from django import forms

from documents.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'standard', 'file']
