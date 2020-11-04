from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from crud_project.client.forms import InsereClientForm
from crud_project.client.models import Client


class ClientListView(ListView):
    template_name = "client/lista.html"
    model = Client
    context_object_name = "cliente"


class ClientUpdateView(UpdateView):
    template_name = 'client/atualiza.html'
    model = Client
    fields = [
        'nome',
        'endereco',
        'telefone',
        'data_nascimento',
    ]


class ClientDeleteView(DeleteView):
    template_name = 'client/exclui.html'
    model = Client
    context_object_name = 'cliente'
    success_url = reverse_lazy("client:lista_cliente")


class ClientCreateView(CreateView):
    template_name = "client/cria.html"
    model = Client
    form_class = InsereClientForm
    success_url = reverse_lazy("client:lista_cliente")


class ClientDadosUpdateView(UpdateView):
    template_name = 'client/dados_cliente.html'
    model = Client
    fields = '__all__'
    context_object_name = 'client'

