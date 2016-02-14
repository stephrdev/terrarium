# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models  # noqa


class Migration(migrations.Migration):

    dependencies = [
        ('watchdog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchdog',
            options={'verbose_name_plural': 'Watchdogs', 'verbose_name': 'Watchdog', 'permissions': (('check_watchdog', 'Can check Watchdog'),), 'ordering': ('metric',)},
        ),
    ]
