# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20190516_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
