from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from reagents.forms import ReagentForm
from reagents.models import Reagent
from reagents.utils import reagents_table_xlsx


@permission_required('reagents.view_reagent', raise_exception=True)
def reagent_index(request):
    context = {
        'page_obj': Reagent.objects.all(),
    }
    return render(request, 'reagents/index.html', context)


@permission_required('reagents.add_reagent', raise_exception=True)
def reagent_create(request):
    form = ReagentForm(
        request.POST or None,
    )
    if not form.is_valid():
        return render(request,
                      'reagents/reagent_create_edit.html', {'form': form})
    reagent = form.save()
    messages.success(request, 'Реактив успешно создан')
    return redirect('reagents:edit', reagent_id=reagent.id)


@permission_required('reagents.change_reagent', raise_exception=True)
def reagent_edit(request, reagent_id):
    reagent = get_object_or_404(Reagent, id=reagent_id)
    form = ReagentForm(
        request.POST or None,
        instance=reagent,
    )
    context = {
        'form': form,
        'reagent': reagent,
        'is_edit': True,
    }
    if not form.is_valid():
        return render(request, 'reagents/reagent_create_edit.html', context)
    form.save()
    messages.success(request, 'Реактив успешно изменен')
    return redirect('reagents:edit', reagent_id=reagent_id)


@permission_required('reagents.delete_reagent', raise_exception=True)
@require_http_methods(["POST"])
def reagent_delete(request, reagent_id):
    reagent = get_object_or_404(Reagent, id=reagent_id)
    reagent.delete()
    return redirect('reagents:index')


@permission_required('reagents.view_reagent', raise_exception=True)
def reagents_table(request):
    return reagents_table_xlsx()
