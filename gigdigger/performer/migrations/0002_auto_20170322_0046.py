# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30, verbose_name='location string'),
        ),
        migrations.AlterField(
            model_name='user',
            name='soundcloud',
            field=models.CharField(blank=True, max_length=30, verbose_name='soundcloud link'),
        ),
        migrations.AlterField(
            model_name='user',
            name='youtube',
            field=models.CharField(blank=True, max_length=30, verbose_name='youtube link'),
        ),
    ]