# Generated by Django 4.1.9 on 2023-06-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registromodel',
            name='professor',
            field=models.CharField(choices=[('professor1', 'Professor 1'), ('professor2', 'Professor 2'), ('professor3', 'Professor 3')], max_length=100, verbose_name='Nome Professor'),
        ),
    ]
