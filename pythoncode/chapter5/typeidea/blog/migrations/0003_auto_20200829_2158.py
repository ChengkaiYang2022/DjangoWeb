# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-08-29 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(blank=True, max_length=1024, verbose_name='描述'),
        ),
    ]
