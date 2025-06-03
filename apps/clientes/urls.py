from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('adicionar/', views.add_client, name='add_client'),
    path('', views.list_clients, name='list_clients'),
    path('editar/<int:id_client>/', views.edit_client, name='edit_client'),
    path('excluir/<int:id_client>/', views.delete_client, name='delete_client'),
]