from django import forms
from .models import Bibliotecario

class BibliotecarioForm(forms.ModelForm):

    class Meta:
        model = Bibliotecario
        exclude = ()