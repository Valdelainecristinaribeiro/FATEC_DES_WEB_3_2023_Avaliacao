# Generated by Django 4.1.9 on 2023-06-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Aluno')),
                ('professor', models.CharField(max_length=100, verbose_name='Nome Professor')),
            ],
        ),
    ]
