from django.shortcuts import render


def permission_denied(request, exception):
    return render(request, 'core/403.html', {'path': request.path}, status=403)


def page_not_found(request, exception):
    return render(request, 'core/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'core/500.html', {'path': request.path}, status=500)


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html')
