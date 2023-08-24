from django.urls import path

from reagents import views


app_name = 'reagents'
urlpatterns = [
    path('', views.index, name='index'),
]
