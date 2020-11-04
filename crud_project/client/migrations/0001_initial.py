# Generated by Django 3.1.3 on 2020-11-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
