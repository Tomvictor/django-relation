# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20160724_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='date_of_birth',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
