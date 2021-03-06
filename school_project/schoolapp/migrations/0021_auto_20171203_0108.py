# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-02 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0020_alumnistudent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='acheiver',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='gallary',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
