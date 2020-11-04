from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class Client(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(help_text='16/11/1996')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('client:dados_cliente', kwargs={'slug': self.slug})
