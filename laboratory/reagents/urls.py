from django.urls import path

from reagents import views


app_name = 'reagents'
urlpatterns = [
    path('', views.reagent_index, name='index'),
    path('create/', views.reagent_create, name='create'),
    path('<int:reagent_id>/', views.reagent_edit, name='edit'),
    path('<int:reagent_id>/delete/', views.reagent_delete, name='delete'),
]
