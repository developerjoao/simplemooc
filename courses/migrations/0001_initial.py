# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descricao')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de Inicio')),
                ('image', models.ImageField(upload_to='courses/images', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Criado em ')),
            ],
        ),
    ]
