# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_interior_designer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carpainter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Person_name', models.CharField(max_length=75)),
                ('Person_phn_no', models.CharField(max_length=10)),
                ('Person_address', models.CharField(max_length=300)),
                ('Person_rate', models.IntegerField(default=0)),
                ('Person_status', models.CharField(max_length=30)),
                ('Person_date', models.DateField()),
                ('Person_timing', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Person_name', models.CharField(max_length=75)),
                ('Person_phn_no', models.CharField(max_length=10)),
                ('Person_address', models.CharField(max_length=300)),
                ('Person_rate', models.IntegerField(default=0)),
                ('Person_status', models.CharField(max_length=30)),
                ('Person_date', models.DateField()),
                ('Person_timing', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
