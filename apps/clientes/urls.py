from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('adicionar/', views.add_cliente, name='add_cliente'),
    path('', views.list_clientes, name='list_clientes'),
    path('editar/<int:id_cliente>/', views.edit_cliente, name='edit_cliente'),
    path('excluir/<int:id_cliente>/', views.delete_cliente, name='delete_cliente'),
    path('buscar/', views.search_clientes, name='search_clientes'),
]