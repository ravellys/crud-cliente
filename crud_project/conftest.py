import pytest
from model_mommy import mommy


# criado para testes com o usuário logado
@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_model = mommy.make(django_user_model, first_name='fulano')
    return usuario_model


@pytest.fixture
def cliente_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client
