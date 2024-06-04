from django.urls import path

from documents import views


app_name = 'documents'
urlpatterns = [
    path('', views.document_index, name='index'),
    path('create/', views.document_create, name='create'),
    path('<int:document_id>/', views.document_edit, name='edit'),
    path('<int:document_id>/delete/', views.document_delete, name='delete'),
]
