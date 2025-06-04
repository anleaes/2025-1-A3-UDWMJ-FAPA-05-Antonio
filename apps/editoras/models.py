from django.db import models

# Create your models here.

class Editora(models.Model):
    name = models.CharField('Nome', max_length=50)
    since_year = models.IntegerField('Ano de Fundacao',null=True, blank=True,default=0)

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering =['id']

    def __str__(self):
        return self.name