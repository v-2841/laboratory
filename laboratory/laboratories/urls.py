from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'laboratories'
urlpatterns = [
    path('', TemplateView.as_view(template_name='laboratories/main.html'),
         name="main"),
]
