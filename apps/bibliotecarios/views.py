from django.shortcuts import render, redirect, get_object_or_404

from .forms import BibliotecarioForm
from .models import Bibliotecario
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_bibliotecario(request):
    template_name = 'bibliotecarios/add_bibliotecario.html'
    context = {}
    if request.method == 'POST':
        form = BibliotecarioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('bibliotecarios:list_bibliotecarios')
    form = BibliotecarioForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_bibliotecarios(request):
    template_name = 'bibliotecarios/list_bibliotecarios.html'
    bibliotecarios = Bibliotecario.objects.filter()
    context = {
        'bibliotecarios': bibliotecarios
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_bibliotecario(request, id_bibliotecario):
    template_name = 'bibliotecarios/add_bibliotecario.html'
    context ={}
    bibliotecario = get_object_or_404(Bibliotecario, id=id_bibliotecario)
    if request.method == 'POST':
        form = BibliotecarioForm(request.POST, instance=bibliotecario)
        if form.is_valid():
            form.save()
            return redirect('bibliotecarios:list_bibliotecarios')
    form = BibliotecarioForm(instance=bibliotecario)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_bibliotecario(request, id_bibliotecario):
    bibliotecario = Bibliotecario.objects.get(id=id_bibliotecario)
    bibliotecario.delete()
    return redirect('bibliotecarios:list_bibliotecarios')