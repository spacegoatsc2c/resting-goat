# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 22:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_type', models.CharField(max_length=50)),
                ('tags', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=2083, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=50)),
                ('is_dead', models.BooleanField(default=False)),
                ('guide', models.CharField(blank=True, max_length=50, null=True)),
                ('ordering', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('realm', models.CharField(max_length=50)),
                ('ilvl', models.IntegerField()),
                ('tradeskill1', models.CharField(blank=True, max_length=50, null=True)),
                ('tradeskill2', models.CharField(blank=True, max_length=50, null=True)),
                ('wowclass', models.CharField(max_length=50)),
                ('portrait', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Raid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=50)),
                ('tier', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='boss',
            name='raid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Raid'),
        ),
        migrations.AddField(
            model_name='article',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Boss'),
        ),
        migrations.AddField(
            model_name='article',
            name='character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Character'),
        ),
    ]
