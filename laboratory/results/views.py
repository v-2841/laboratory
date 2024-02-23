from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render

from results.forms import ResultForm, ResultNutritionForm
from results.models import Result
from results.utils import results_table_xlsx


@permission_required('results.view_result', raise_exception=True)
def result_index(request):
    results = Result.objects.order_by(
        '-pub_date').prefetch_related('researcher')[:250]
    not_processed = sum(
        1 for result in results if not result.is_processed)
    context = {
        'page_obj': results,
        'not_processed': not_processed,
    }
    return render(request, 'results/index.html', context)


@permission_required('results.add_result', raise_exception=True)
def result_create(request):
    form = ResultForm(
        request.POST or None,
    )
    if not form.is_valid():
        return render(request, 'results/result_create.html', {'form': form})
    result = form.save(commit=False)
    result.researcher = request.user
    result.save()
    messages.success(request, 'Результат исследования успешно создан')
    return render(request, 'results/result_create.html',
                  {'form': ResultForm(initial={
                      'sample_name': form.cleaned_data['sample_name']})})


@permission_required('results.add_result', raise_exception=True)
def result_nutrition_create(request):
    form = ResultNutritionForm(
        request.POST or None,
    )
    if not form.is_valid():
        return render(request,
                      'results/result_nutrition_create.html', {'form': form})
    Result.objects.create(
        sample_name=form.cleaned_data['sample_name'],
        analysis_name='Массовая доля жира',
        standard=form.cleaned_data['fat_standard'],
        measurement_unit='%',
        result=form.cleaned_data['fat'],
        researcher=request.user,
    )
    Result.objects.create(
        sample_name=form.cleaned_data['sample_name'],
        analysis_name='Массовая доля белка',
        standard=form.cleaned_data['protein_standard'],
        measurement_unit='%',
        result=form.cleaned_data['protein'],
        researcher=request.user,
    )
    Result.objects.create(
        sample_name=form.cleaned_data['sample_name'],
        analysis_name='Массовая доля углеводов',
        standard=form.cleaned_data['carbohydrate_standard'],
        measurement_unit='%',
        result=form.cleaned_data['carbohydrate'],
        researcher=request.user,
    )
    if not form.cleaned_data['energy_value']:
        form.cleaned_data['energy_value'] = round(
            form.cleaned_data['fat'] * form.cleaned_data['fat_multiplier']
            + form.cleaned_data['protein']
            * form.cleaned_data['protein_multiplier']
            + form.cleaned_data['carbohydrate']
            * form.cleaned_data['carbohydrate_multiplier']
        )
    Result.objects.create(
        sample_name=form.cleaned_data['sample_name'],
        analysis_name='Энергетическая ценность',
        standard=form.cleaned_data['energy_value_standard'],
        measurement_unit='ккал/100 г',
        result=form.cleaned_data['energy_value'],
        researcher=request.user,
    )
    return redirect('results:index')


@permission_required('results.change_result', raise_exception=True)
def result_edit(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    result.is_processed = True
    result.save()
    return redirect('results:index')


@permission_required('results.view_result', raise_exception=True)
def marked_results_table(request):
    marked_results = request.GET.get('results', None)
    if marked_results:
        marked_results = marked_results.split(',')
        return results_table_xlsx(marked_results)
    else:
        return redirect('results:index')


@permission_required('results.view_result', raise_exception=True)
def results_table(request):
    return results_table_xlsx()
