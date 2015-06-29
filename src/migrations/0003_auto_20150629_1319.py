# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20150629_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electrician',
            old_name='helper_address',
            new_name='elect_address',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='helper_date',
            new_name='elect_date',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='helper_name',
            new_name='elect_name',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='helper_phn_no',
            new_name='elect_phn_no',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='helper_rate',
            new_name='elect_rate',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='helper_status',
            new_name='elect_status',
        ),
        migrations.RenameField(
            model_name='electrician',
            old_name='helper_timing',
            new_name='elect_timing',
        ),
    ]
