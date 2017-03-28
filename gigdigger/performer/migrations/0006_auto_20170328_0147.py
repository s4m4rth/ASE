# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performer', '0005_auto_20170322_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=30, verbose_name='address string'),
        ),
        migrations.AddField(
            model_name='user',
            name='capacity',
            field=models.CharField(blank=True, max_length=30, verbose_name='capacity string'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, max_length=30, verbose_name='description string'),
        ),
    ]