from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def listar(request):
    clientes = Cliente.objects.all().order_by('id')
    context = {'clientes': clientes}
    return render(request, 'lista.html', context=context)


def detalhes(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    context = {'cliente': cliente}
    return render(request, 'detalhes.html', context=context)


def cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastro com sucesso!')
            return redirect('listar')
    else:
        form = ClienteForm()

    return render(request, 'cadastro.html', {'form': form})


def alterar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    form = ClienteForm(instance=cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente alterado com sucesso!')
            return redirect('listar')

    context = {'cliente': cliente, 'form': form}
    return render(request, 'alterar.html', context=context)


def excluir(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    messages.success(request, 'Cliente excluído com sucesso!')
    return redirect('listar')
