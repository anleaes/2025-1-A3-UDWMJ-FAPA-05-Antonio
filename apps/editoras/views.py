from django.shortcuts import render, redirect, get_object_or_404

from .forms import EditoraForm
from .models import Editora

# Create your views here.

def add_editora(request):
    template_name = 'editoras/add_editora.html'
    context = {}
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('editoras:list_editoras')
    form = EditoraForm()
    context['form'] = form
    return render(request, template_name, context)

def list_editoras(request):
    template_name = 'editoras/list_editoras.html'
    editoras = Editora.objects.filter()
    context = {
        'editoras': editoras
    }
    return render(request, template_name, context)

def edit_editora(request, id_editora):
    template_name = 'editoras/add_editora.html'
    context ={}
    editora = get_object_or_404(Editora, id=id_editora)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('editoras:list_editoras')
    form = EditoraForm(instance=editora)
    context['form'] = form
    return render(request, template_name, context)

def delete_editora(request, id_editora):
    editora = Editora.objects.get(id=id_editora)
    editora.delete()
    return redirect('editoras:list_editoras')