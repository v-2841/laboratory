from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api.views import ReagentViewSet


router = DefaultRouter()
router.register(r'reagents', ReagentViewSet, basename='reagents')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
