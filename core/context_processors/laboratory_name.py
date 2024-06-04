from laboratories.models import Laboratory


def laboratory_name(request):
    try:
        name = Laboratory.objects.first().name
    except Exception:
        name = 'Laboratory'
    return {
        'laboratory_name': name
    }
