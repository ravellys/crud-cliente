import pytest
from django.urls import reverse

from crud_project.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}"')


def test_lista_clientes_link(resp):
    assert_contains(resp, f'href="{reverse("client:lista_cliente")}"')


def test_cadastro_clientes_link(resp):
    assert_contains(resp, f'href="{reverse("client:cadastra_cliente")}"')


def test_portifolio_link(resp):
    assert_contains(resp, 'href="https://ravellys.github.io"')
