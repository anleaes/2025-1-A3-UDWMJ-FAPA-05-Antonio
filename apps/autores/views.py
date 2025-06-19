from django.shortcuts import render, redirect, get_object_or_404

from .forms import AutorForm
from .models import Autor

# Create your views here.

def add_autor(request):
    template_name = 'autores/add_autor.html'
    context = {}
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('autores:list_autores')
    form = AutorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_autores(request):
    template_name = 'autores/list_autores.html'
    autores = Autor.objects.filter()
    context = {
        'autores': autores
    }
    return render(request, template_name, context)

def edit_autor(request, id_autor):
    template_name = 'autores/add_autor.html'
    context ={}
    autor = get_object_or_404(Autor, id=id_autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores:list_autores')
    form = AutorForm(instance=autor)
    context['form'] = form
    return render(request, template_name, context)

def delete_autor(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    autor.delete()
    return redirect('autores:list_autores')