from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cliente


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def listar(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'lista.html', context=context)
