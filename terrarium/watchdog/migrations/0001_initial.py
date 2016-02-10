# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didadata', '0002_auto_20151201_1939'),
        ('howl', '0003_alert_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchdog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('max_age', models.PositiveIntegerField(blank=True, null=True)),
                ('metric', models.ForeignKey(to='didadata.Metric')),
                ('observer', models.ForeignKey(to='howl.Observer')),
            ],
            options={
                'ordering': ('metric',),
                'verbose_name': 'Watchdog',
                'verbose_name_plural': 'Watchdogs',
            },
        ),
    ]
