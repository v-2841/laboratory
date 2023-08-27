from django.urls import path

from results import views


app_name = 'results'
urlpatterns = [
    path('', views.result_index, name='index'),
    path('create/', views.result_create, name='create'),
    path('<int:result_id>/', views.result_edit, name='edit'),
]
