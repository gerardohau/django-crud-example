# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]