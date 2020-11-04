# CRUD de clientes
📜 Este repositório trata-se de um projeto para realizar o CRUD (Create, Read, Update, Delete) de clientes com o framework Django. Utilizou-se o método da Class Based Views (CBV) para automatizar e facilitar o encapsulamento das funcionalidades. Para a realização dos testes foi utilizado o pytest-django e como ambiente virtual utilizou-se o pipenv. Por fim, o projeto foi posto em produção no heroku e para seus arquivos estáticos foi feito um bucket na S3 da amazon. 

link do deploy: [crud-cliente](https://crudclienteravellys.herokuapp.com/)

[![Build Status](https://travis-ci.com/ravellys/crud-cliente.svg?branch=master)](https://travis-ci.com/ravellys/crud-cliente)
[![Updates](https://pyup.io/repos/github/ravellys/crud-cliente/shield.svg)](https://pyup.io/repos/github/ravellys/crud-cliente/)
[![Python 3](https://pyup.io/repos/github/ravellys/crud-cliente/python-3-shield.svg)](https://pyup.io/repos/github/ravellys/crud-cliente/)
 
## 💻 Configuração para Desenvolvimento

1. Inicialmente insira como variaveis globais no sistema:
```
PIPENV_VENV_IN_PROJECT=1
PIPENV_IGNORE_VIRTUALENVS=1
```

2. Instale o pipenv
```
pip install pipenv
```

3. Instale as dependências de desenvolvimento
```
pipenv sync -d
```

4. crie um arquivo em .venv/Scripts com o nome _mng.bat_ e conteúdo:
```
@python "%VIRTUAL_ENV%\..\manage.py" %*
```

5. Crie um arquivo _.env_ com as configurações presentes em _contrib/env-sample_

6. Verifique a formatação do código segundo a PEP8 com o flake8 
```
pipenv run flake8 .
```

7. Execute os testes 
```
pipenv run pytest
```

8. Ative o shell do pipenv no seu prompt de comando:
```
pipenv shel
```

9. Execute o projeto:
```
mng runserver
```

10. realize as migrações para se banco de dados:
```
mng makemigrations
mng migrate
```

11. Para criar o super usuário no se banco de dado utilize:
```
mng createsuper user
```

## 🗃 Histórico de lançamentos

* 11/04/2020 Criação do Projeto


## 📋 Meta

Lucas Ravelllys – [Portifólio](https://ravellys.github.io)

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.


## 🚀 Contribuições

1. Faça o _fork_ do projeto (<https://github.com/ravellys/crud-cliente/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

