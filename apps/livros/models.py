from django.db import models
from categorias.models import Categoria
from editoras.models import Editora
from autores.models import Autor

# Create your models here.

class Livro(models.Model):
    title = models.CharField('Titulo', max_length=50)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    livro_category = models.ManyToManyField(Categoria, through='LivroCategoria', blank=True)
    editor = models.ForeignKey(Editora, on_delete=models.CASCADE)
    release_date = models.DateField('Data Publicacao', auto_now=False, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering =['id']

    def __str__(self):
        return self.title
    
class LivroCategoria(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de categoria'
        verbose_name_plural = 'Itens de categorias'
        ordering =['id']

    def __str__(self):
        return self.category.name