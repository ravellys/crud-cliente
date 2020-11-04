from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from crud_project.client.forms import InsereClientForm
from crud_project.client.models import Client


# Lista os clientes cadastrados
class ClientListView(ListView):
    template_name = "client/lista.html"
    model = Client
    context_object_name = "cliente"


# Lista atualiza os dados cadastrais dos clientes
class ClientUpdateView(UpdateView):
    template_name = 'client/atualiza.html'
    model = Client
    fields = [
        'nome',
        'endereco',
        'telefone',
        'data_nascimento',
    ]


# Lista exclui cliente
class ClientDeleteView(DeleteView):
    template_name = 'client/exclui.html'
    model = Client
    context_object_name = 'cliente'
    success_url = reverse_lazy("client:lista_cliente")


# Lista cria cliente
class ClientCreateView(CreateView):
    template_name = "client/cria.html"
    model = Client
    form_class = InsereClientForm
    success_url = reverse_lazy("client:lista_cliente")


# detalhe dos dados de um cliente
class ClientDadosUpdateView(UpdateView):
    template_name = 'client/dados_cliente.html'
    model = Client
    fields = '__all__'
    context_object_name = 'client'
