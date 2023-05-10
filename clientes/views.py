from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def listar(request):
    clientes = Cliente.objects.all()
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
            return redirect('listar')
    else:
        form = ClienteForm()

    return render(request, 'cadastro.html', {'form': form})
