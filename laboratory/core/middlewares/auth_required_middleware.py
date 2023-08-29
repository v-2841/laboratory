import re

from django.shortcuts import redirect
from django.urls import reverse


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (not request.user.is_authenticated
                and request.path != reverse('users:login')
                and request.path != reverse('laboratories:main')
                and not re.match(r'^/admin/', request.path)):
            return redirect(
                f"{reverse('users:login')}?next={request.path}")
        return self.get_response(request)
