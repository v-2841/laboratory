from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from results.forms import ResultForm
from results.models import Result


@permission_required('results.view_result', raise_exception=True)
def result_index(request):
    context = {
        'page_obj': Result.objects.all(),
        'not_processed': Result.objects.filter(is_processed=False).count(),
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


@permission_required('results.change_result', raise_exception=True)
def result_edit(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    result.is_processed = True
    result.save()
    return redirect('results:index')
