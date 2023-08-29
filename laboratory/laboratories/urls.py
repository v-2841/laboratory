from django.urls import path

from laboratories import views


app_name = 'laboratories'
urlpatterns = [
    path('', views.laboratory_main, name="main"),
]
