# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0009_auto_20171116_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallary',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='gallary',
            name='image',
        ),
        migrations.RemoveField(
            model_name='gallary',
            name='width_field',
        ),
    ]
