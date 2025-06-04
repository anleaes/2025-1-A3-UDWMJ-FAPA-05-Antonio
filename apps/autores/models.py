from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField('Nome', max_length=50)
    age = models.IntegerField('Idade',null=True, blank=True,default=0)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering =['id']

    def __str__(self):
        return self.name