from django.db import models
from clientes.models import Cliente
from livros.models import Livro
from bibliotecarios.models import Bibliotecario

# Create your models here.

class Emprestimo(models.Model):
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE)
    item_emprestimo = models.ManyToManyField(Livro, through='ItemEmprestimo', blank=True)
    start_date = models.DateField('Data de inicio', auto_now=False, auto_now_add=False)
    end_date = models.DateField('Prazo de entrega', auto_now=False, auto_now_add=False)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    
    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering =['id']

    def __str__(self):
        return f"emprestimo de {self.client.last_name}"


class ItemEmprestimo(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de emprestimo'
        verbose_name_plural = 'Itens de emprestimo'
        ordering =['id']

    def __str__(self):
        return self.livro.title