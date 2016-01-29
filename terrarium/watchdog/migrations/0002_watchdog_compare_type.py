# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchdog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchdog',
            name='compare_type',
            field=models.PositiveIntegerField(verbose_name='Compate type', choices=[(0, 'Compare value'), (1, 'Compare time')], default=0),
        ),
    ]
