from django import forms

from reagents.models import Reagent


class ReagentForm(forms.ModelForm):
    class Meta:
        model = Reagent
        fields = ['index', 'name', 'grade', 'amount', 'manufacture_date',
                  'expiration_date']
