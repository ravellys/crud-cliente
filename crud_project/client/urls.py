from django.contrib.auth.decorators import login_required
from django.urls import path

from crud_project.client.views import ClientListView, ClientUpdateView, ClientDeleteView, ClientCreateView, \
    ClientDadosUpdateView

app_name = 'client'
urlpatterns = [
    path('clientes/', login_required(ClientListView.as_view()), name='lista_cliente'),
    path('clientes/atualiza/<slug:slug>', login_required(ClientUpdateView.as_view()), name='atualiza_cliente'),
    path('clientes/excluir/<slug:slug>', login_required(ClientDeleteView.as_view()), name='deleta_cliente'),
    path('clientes/cadastrar/', login_required(ClientCreateView.as_view()), name='cadastra_cliente'),
    path('clientes/<slug:slug>', login_required(ClientDadosUpdateView.as_view()), name='dados_cliente'),
]
