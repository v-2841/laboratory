from django.shortcuts import render

from laboratories.models import Laboratory


def laboratory_main(request):
    if Laboratory.objects.all().count() == 0:
        Laboratory.objects.create(
            name='Laboratory',
            description='Добавьте описание в администраторской зоне',
        )
    context = {
        'description': Laboratory.objects.first().description,
    }
    return render(request, 'laboratories/main.html', context)
