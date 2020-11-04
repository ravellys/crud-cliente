import pytest
from django.urls import reverse
from model_mommy import mommy

from crud_project.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


# criação de um usuário
@pytest.fixture
def usuario(db, django_user_model):
    usuario_model = mommy.make(django_user_model)
    senha = 'senha'
    usuario_model.set_password(senha)
    usuario_model.save()
    usuario_model.senha_plana = senha
    return usuario_model


# redirecionamento para o login
@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'),
                       {'username': usuario.email, 'password': usuario.senha_plana})


# testa o redirecionamento para o login
def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('base:home')


# usuário não logado
@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


# Verifica a presença do botão entrar
def test_botao_entrar_disponivel(resp_home):
    assert_contains(resp_home, 'Entrar')


# Verifica a presença do link de login
def test_link_disponivel(resp_home):
    assert_contains(resp_home, reverse('login'))


# usuário logado
@pytest.fixture
def resp_home_logado(cliente_com_usuario_logado):
    return cliente_com_usuario_logado.get(reverse('base:home'))


# Verifica que não há o botão de entrar
def test_botao_entrar_indisponivel(resp_home_logado):
    assert_not_contains(resp_home_logado, 'Entrar')


# Verifica que não há o link de entrar
def test_link_indisponivel(resp_home_logado):
    assert_not_contains(resp_home_logado, reverse('login'))


# Verifica que há o botão para sair
def test_botao_sair_disponivel(resp_home_logado):
    assert_contains(resp_home_logado, 'Sair')


# Verifica o nome do usuário que esta logado
def test_nome_usuario_logado_disponivel(resp_home_logado, usuario_logado):
    assert_contains(resp_home_logado, usuario_logado.first_name)


# Verifica que há o link para logout
def test_link_logout_disponivel(resp_home_logado):
    assert_contains(resp_home_logado, reverse('logout'))
