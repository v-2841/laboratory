from django.shortcuts import render

from reagents.models import Reagent


def index(request):
    context = {
        'page_obj': Reagent.objects.all(),
    }
    return render(request, 'reagents/index.html', context)
