# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20150629_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electrician',
            old_name='elect_address',
            new_name='Person_address',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='elect_date',
            new_name='Person_date',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='elect_name',
            new_name='Person_name',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='elect_phn_no',
            new_name='Person_phn_no',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='elect_rate',
            new_name='Person_rate',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='elect_status',
            new_name='Person_status',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='elect_timing',
            new_name='Person_timing',
        ),
    ]
