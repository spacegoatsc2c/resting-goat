# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boss',
            name='guide',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='boss',
            name='logo',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='character',
            name='portrait',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='raid',
            name='logo',
            field=models.CharField(max_length=2000),
        ),
    ]