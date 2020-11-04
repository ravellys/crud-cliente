from django import forms

from crud_project.client.models import Client


# Cria o Formulário de acordo com o modelo
class InsereClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = [
            'nome',
            'endereco',
            'telefone',
            'data_nascimento',
        ]
