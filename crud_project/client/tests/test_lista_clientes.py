import pytest
from django.urls import reverse
from model_mommy import mommy

from crud_project.django_assertions import assert_contains
from crud_project.client.models import Client


@pytest.fixture
def cliente(db):
    return mommy.make(Client, 3)


@pytest.fixture
def resp(cliente_com_usuario_logado, cliente):
    return cliente_com_usuario_logado.get(reverse('client:lista_cliente'))


def test_lista_disponivel(resp):
    assert resp.status_code == 200


def test_dados(resp, cliente):
    for c in cliente:
        assert_contains(resp, c.nome,)
        assert_contains(resp, c.telefone,)
        assert_contains(resp, c.endereco,)


def test_link_alterar(resp, cliente):
    for c in cliente:
        assert_contains(resp, reverse('client:atualiza_cliente', kwargs={'slug': c.slug}))


def test_link_deletar(resp, cliente):
    for c in cliente:
        assert_contains(resp, reverse('client:deleta_cliente', kwargs={'slug': c.slug}))


def test_link_cadastrar(resp, cliente):
    assert_contains(resp, reverse('client:cadastra_cliente'))
