from django.urls import path
from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('', views.list_emprestimos, name='list_emprestimos'),
    path('adicionar/<int:id_cliente>/', views.add_emprestimo, name='add_emprestimo'),
    path('excluir/<int:id_emprestimo>/', views.delete_emprestimo, name='delete_emprestimo'),
    path('excluir-item/<int:id_emprestimo_item>/', views.delete_emprestimo_item, name='delete_emprestimo_item'),
    path('adicionar-item/<int:id_emprestimo>/', views.add_emprestimo_item, name='add_emprestimo_item'),
    path('editar-status/<int:id_emprestimo>/', views.edit_emprestimo_status, name='edit_emprestimo_status'),
]