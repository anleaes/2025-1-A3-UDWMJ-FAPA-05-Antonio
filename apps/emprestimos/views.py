from django.shortcuts import render, redirect, get_object_or_404

from .forms import EmprestimoForm, ItemEmprestimoForm
from .models import Emprestimo , ItemEmprestimo, Livro, Cliente

# Create your views here.

def add_emprestimo(request, id_cliente):
    template_name = 'emprestimos/add_emprestimo.html'
    context = {}
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.cliente = Cliente.objects.get(id=id_cliente)
            f.save()
            form.save_m2m()
            return redirect('emprestimos:list_emprestimos')
    form = EmprestimoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_emprestimos(request):
    template_name = 'emprestimos/list_emprestimos.html'
    emprestimos = Emprestimo.objects.filter()
    emprestimo_items = ItemEmprestimo.objects.filter()
    livros = Livro.objects.filter()
    clientes = Cliente.objects.filter()
    context = {
        'emprestimos': emprestimos,
        'emprestimo_items': emprestimo_items,
        'livros': livros,
        'clientes': clientes
    }
    return render(request, template_name, context)

def delete_emprestimo(request, id_emprestimo):
    emprestimo = Emprestimo.objects.get(id=id_emprestimo)
    emprestimo.delete()
    return redirect('emprestimos:list_emprestimos')

def add_emprestimo_item(request, id_emprestimo):
    template_name = 'emprestimos/add_emprestimo_item.html'
    context = {}
    if request.method == 'POST':
        form = ItemEmprestimoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.emprestimo = Emprestimo.objects.get(id=id_emprestimo)
            f.save()
            form.save_m2m()
            return redirect('emprestimos:list_emprestimos')
    form = ItemEmprestimoForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_emprestimo_item(request, id_emprestimo_item):
    emprestimoitem = ItemEmprestimo.objects.get(id=id_emprestimo_item)
    emprestimoitem.delete()
    return redirect('emprestimos:list_emprestimos')

def edit_emprestimo_status(request, id_emprestimo):
    template_name = 'emprestimos/edit_emprestimo_status.html'
    context ={}
    emprestimo = get_object_or_404(Emprestimo, id=id_emprestimo)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimos:list_emprestimos')
    form = EmprestimoForm(instance=emprestimo)
    context['form'] = form
    return render(request, template_name, context)