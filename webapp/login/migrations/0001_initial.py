# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-01 21:53
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
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier_titre', models.CharField(max_length=500)),
                ('fichier_description', models.CharField(max_length=1000)),
                ('fichier_file', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_infos', models.CharField(max_length=1000)),
                ('user_logo', models.FileField(upload_to='')),
                ('slug', models.SlugField(unique=True)),
                ('usager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doc',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Personne'),
        ),
    ]
