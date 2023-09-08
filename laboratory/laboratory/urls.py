from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('reagents/', include('reagents.urls', namespace='reagents')),
    path('results/', include('results.urls', namespace='results')),
    path('documents/', include('documents.urls', namespace='documents')),
    path('', include('laboratories.urls', namespace='laboratories')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
