# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appesi', '0002_tipocursomod'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursomod',
            name='tipocursof',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appesi.Tipocursomod'),
        ),
    ]
