# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performer', '0003_auto_20170326_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='performer_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venueid',
            field=models.CharField(max_length=30),
        ),
    ]