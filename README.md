# crud-cliente
📜 Este repositório trata-se de um projeto para realizar o CRUD (Create, Read, Update, Delete) de clientes com o framework Django.

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

3. Instale as dependencias d desenvolvimento
```
pipenv sync -d
```

4. Crie um arquivo .env com as configurações presentes em env-sample

5. Verifique a PEP8 com o flake8 
```
pipenv run flake8 .
```

5. Execute os testes 
```
pipenv run pytest
```

## 🗃 Histórico de lançamentos

* 11/04/2020 Criação do Projeto


## 📋 Meta

Lucas Ravelllys – [@ravellys](https://ravellys.github.io)

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.


## 🚀 Contribuições

1. Faça o _fork_ do projeto (<https://github.com/ravellys/crud-cliente/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

