from django import forms
from .models import Emprestimo, Cliente, ItemEmprestimo ,Livro

class EmprestimoForm(forms.ModelForm):
    
    class Meta:
        model = Emprestimo
        exclude = ('cliente',)

class ItemEmprestimoForm(forms.ModelForm):
    
    class Meta:
        model = ItemEmprestimo
        exclude = ('emprestimo',)