from django import forms

from results.models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['sample_name', 'analysis_name', 'standard',
                  'measurement_unit', 'result']


class ResultNutritionForm(forms.Form):
    sample_name = forms.CharField(
        max_length=200,
        label='Название образца',
    )
    fat = forms.DecimalField(
        min_value=0,
        max_value=100,
        max_digits=4,
        decimal_places=2,
        label='Жиры',
    )
    fat_standard = forms.CharField(
        max_length=200,
        label='Нормативный документ для измерения м.д. жира',
    )
    fat_multiplier = forms.DecimalField(
        min_value=0,
        initial=9,
        label='Коэффициент для жира',
    )
    protein = forms.DecimalField(
        min_value=0,
        max_value=100,
        max_digits=4,
        decimal_places=2,
        label='Белки',
    )
    protein_standard = forms.CharField(
        max_length=200,
        label='Нормативный документ для измерения м.д. белка',
    )
    protein_multiplier = forms.DecimalField(
        min_value=0,
        initial=4,
        label='Коэффициент для белка',
    )
    carbohydrate = forms.DecimalField(
        min_value=0,
        max_value=100,
        max_digits=4,
        decimal_places=2,
        label='Углеводы',
    )
    carbohydrate_standard = forms.CharField(
        max_length=200,
        label='Нормативный документ для измерения м.д. угдеводов',
    )
    carbohydrate_multiplier = forms.DecimalField(
        min_value=0,
        initial=4,
        label='Коэффициент для углеводов',
    )
    energy_value = forms.IntegerField(
        required=False,
        label='Энергетическая ценность',
    )
    energy_value_standard = forms.CharField(
        max_length=200,
        label='Нормативный документ для вычисления энергетической ценности',
    )

    class Meta:
        localized_fields = '__all__'
