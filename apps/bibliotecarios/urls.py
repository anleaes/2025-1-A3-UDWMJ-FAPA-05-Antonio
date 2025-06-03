from django.urls import path
from . import views

app_name = 'bibliotecarios'

urlpatterns = [
    path('adicionar/', views.add_bibliotecario, name='add_bibliotecario'),
    path('', views.list_bibliotecarios, name='list_bibliotecarios'),
    path('editar/<int:id_bibliotecario>/', views.edit_bibliotecario, name='edit_bibliotecario'),
    path('excluir/<int:id_bibliotecario>/', views.delete_bibliotecario, name='delete_bibliotecario'),
]