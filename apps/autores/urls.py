from django.urls import path
from . import views

app_name = 'autores'

urlpatterns = [
    path('adicionar/', views.add_autor, name='add_autor'),
    path('', views.list_autores, name='list_autores'),
    path('editar/<int:id_autor>/', views.edit_autor, name='edit_autor'),
    path('excluir/<int:id_autor>/', views.delete_autor, name='delete_autor'),
]