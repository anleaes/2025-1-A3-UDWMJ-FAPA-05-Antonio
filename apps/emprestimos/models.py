from django.db import models
from clientes.models import Cliente
from livros.models import Livro

# Create your models here.

class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    item_emprestimo = models.ManyToManyField(Livro, through='ItemEmprestimo', blank=True)
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
        return f"emprestimo de {self.cliente.last_name}"


class ItemEmprestimo(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de emprestimo'
        verbose_name_plural = 'Itens de emprestimo'
        ordering =['id']

    def __str__(self):
        return self.livro.title