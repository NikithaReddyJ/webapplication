# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-09-26 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_table2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table2',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
