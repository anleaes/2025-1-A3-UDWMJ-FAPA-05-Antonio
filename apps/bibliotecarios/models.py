from django.db import models

# Create your models here.

class Bibliotecario(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    SHIFT_CHOICES = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
    )
    shift = models.CharField('Turno', max_length=1, choices=SHIFT_CHOICES)
    
    class Meta:
        verbose_name = 'Bibliotecario'
        verbose_name_plural = 'Bibliotecarios'
        ordering =['id']

    def __str__(self):
        return self.first_name