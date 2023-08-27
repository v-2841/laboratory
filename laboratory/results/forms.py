from django import forms

from results.models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['sample_name', 'analysis_name', 'standard',
                  'measurement_unit', 'result']
