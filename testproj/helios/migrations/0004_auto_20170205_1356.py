# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-05 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0003_service_service_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licence',
            name='invoicedate',
            field=models.DateField(blank=True, max_length=19, null=True),
        ),
    ]
