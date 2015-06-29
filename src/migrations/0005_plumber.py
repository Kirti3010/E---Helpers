# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20150629_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plumber',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Person_name', models.CharField(max_length=75)),
                ('Person_phn_no', models.CharField(max_length=10)),
                ('Person_address', models.CharField(max_length=300)),
                ('Person_rate', models.IntegerField(default=0)),
                ('Person_status', models.CharField(max_length=30)),
                ('Person_date', models.DateField()),
                ('Person_timing', models.TimeField()),
            ],
        ),
    ]
