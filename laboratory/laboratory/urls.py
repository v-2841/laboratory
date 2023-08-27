from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('reagents/', include('reagents.urls', namespace='reagents')),
    path('results/', include('results.urls', namespace='results')),
    path('', include('laboratories.urls', namespace='laboratories')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
