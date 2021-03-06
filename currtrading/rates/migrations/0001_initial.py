# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('curr_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_curr_from', to='rates.Currency')),
                ('curr_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_curr_to', to='rates.Currency')),
            ],
        ),
    ]
