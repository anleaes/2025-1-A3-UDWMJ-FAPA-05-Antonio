from django.urls import path
from . import views

app_name = 'editoras'

urlpatterns = [
    path('adicionar/', views.add_editora, name='add_editora'),
    path('', views.list_editoras, name='list_editoras'),
    path('editar/<int:id_editora>/', views.edit_editora, name='edit_editora'),
    path('excluir/<int:id_editora>/', views.delete_editora, name='delete_editora'),
]