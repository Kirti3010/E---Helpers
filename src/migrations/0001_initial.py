# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helpers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('helper_name', models.CharField(max_length=75)),
                ('helper_phn_no', models.CharField(max_length=10)),
                ('helper_address', models.CharField(max_length=300)),
                ('helper_rate', models.IntegerField(default=0)),
                ('helper_status', models.CharField(max_length=30)),
                ('helper_date', models.DateField()),
                ('helper_timing', models.TimeField()),
            ],
        ),
    ]
