from django.shortcuts import render, redirect, get_object_or_404

from .forms import LivroForm
from .models import Livro, Categoria, LivroCategoria

# Create your views here.

def add_livro(request):
    template_name = 'livros/add_livro.html'
    context = {}
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('livros:list_livros')
    form = LivroForm()
    context['form'] = form
    return render(request, template_name, context)

def list_livros(request):
    template_name = 'livros/list_livros.html'
    livrocategorias = LivroCategoria.objects.filter()
    categorias = Categoria.objects.filter()
    livros = Livro.objects.filter()
    context = {
        'livros': livros,
        'categorias': categorias,
        'livrocategorias': livrocategorias
    }
    return render(request, template_name, context)

def edit_livro(request, id_livro):
    template_name = 'livros/add_livro.html'
    context ={}
    livro = get_object_or_404(Livro, id=id_livro)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livros:list_livros')
    form = LivroForm(instance=livro)
    context['form'] = form
    return render(request, template_name, context)

def delete_livro(request, id_livro):
    livro = Livro.objects.get(id=id_livro)
    livro.delete()
    return redirect('livros:list_livros')