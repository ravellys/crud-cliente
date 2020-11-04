from django import forms

from crud_project.client.models import Client


class InsereClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = [
            'nome',
            'endereco',
            'telefone',
            'data_nascimento',
        ]
