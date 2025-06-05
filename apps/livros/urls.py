from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('adicionar/', views.add_livro, name='add_livro'),
    path('', views.list_livros, name='list_livros'),
    path('editar/<int:id_livro>/', views.edit_livro, name='edit_livro'),
    path('excluir/<int:id_livro>/', views.delete_livro, name='delete_livro'),
]