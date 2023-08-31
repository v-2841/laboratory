from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from documents.forms import DocumentForm
from documents.models import Document


@permission_required('documents.view_document', raise_exception=True)
def document_index(request):
    context = {
        'page_obj': Document.objects.all(),
    }
    return render(request, 'documents/index.html', context)


@permission_required('documents.add_document', raise_exception=True)
def document_create(request):
    form = DocumentForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if not form.is_valid():
        return render(request,
                      'documents/document_create_edit.html', {'form': form})
    document = form.save()
    messages.success(request, 'Документ успешно создан')
    return redirect('documents:edit', document_id=document.id)


@permission_required('documents.change_document', raise_exception=True)
def document_edit(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    form = DocumentForm(
        request.POST or None,
        files=request.FILES or None,
        instance=document,
    )
    context = {
        'form': form,
        'document': document,
        'is_edit': True,
    }
    if not form.is_valid():
        return render(request, 'documents/document_create_edit.html', context)
    form.save()
    messages.success(request, 'Документ успешно изменен')
    return redirect('documents:edit', document_id=document_id)


@permission_required('documents.delete_document', raise_exception=True)
@require_http_methods(["POST"])
def document_delete(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return redirect('documents:index')
