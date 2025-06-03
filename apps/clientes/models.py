from django.db import models

# Create your models here.

class Cliente(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    email = models.EmailField('E-mail',null=False, blank=False)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    address = models.CharField('Endereco', max_length=200)   
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name