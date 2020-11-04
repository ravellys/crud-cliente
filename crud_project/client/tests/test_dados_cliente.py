import pytest
from django.urls import reverse
from model_mommy import mommy
from crud_project.django_assertions import assert_contains
from crud_project.client.models import Client


@pytest.fixture
def cliente(db):
    return mommy.make(Client)


@pytest.fixture
def resp(cliente_com_usuario_logado, cliente):
    resp = cliente_com_usuario_logado.get(reverse('client:dados_cliente', kwargs={'slug': cliente.slug}))
    return resp


def test_dados(resp, cliente: Client):
    assert_contains(resp, cliente.nome)
    assert_contains(resp, cliente.endereco)
    assert_contains(resp, cliente.telefone)


@pytest.fixture
def resp_sem_usuario(client, cliente):
    resp = client.get(reverse('client:dados_cliente', kwargs={'slug': cliente.slug}))
    return resp


def teste_sem_usuario_logado(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))
