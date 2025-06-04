from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('adicionar/', views.add_categoria, name='add_categoria'),
    path('', views.list_categorias, name='list_categorias'),
    path('editar/<int:id_categoria>/', views.edit_categoria, name='edit_categoria'),
    path('excluir/<int:id_categoria>/', views.delete_categoria, name='delete_categoria'),
]