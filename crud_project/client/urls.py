from django.urls import path

from crud_project.client.views import ClientListView, ClientUpdateView, ClientDeleteView, ClientCreateView, \
    ClientDadosUpdateView

app_name = 'client'
urlpatterns = [
    path('clientes/', ClientListView.as_view(), name='lista_cliente'),
    path('clientes/atualiza/<slug:slug>', ClientUpdateView.as_view(), name='atualiza_cliente'),
    path('clientes/excluir/<slug:slug>', ClientDeleteView.as_view(), name='deleta_cliente'),
    path('clientes/cadastrar/', ClientCreateView.as_view(), name='cadastra_cliente'),
    path('clientes/<slug:slug>', ClientDadosUpdateView.as_view(), name='dados_cliente'),
]
