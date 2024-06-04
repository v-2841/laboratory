from django.conf import settings
from django.core.paginator import Paginator


def paginator(request, obj):
    paginator = Paginator(obj, settings.VIEW_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
