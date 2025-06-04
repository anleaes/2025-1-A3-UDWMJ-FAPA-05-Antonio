from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.CharField('Descricao', max_length=200)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name