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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('metric', models.ForeignKey(to='didadata.Metric')),
                ('observer', models.ForeignKey(to='howl.Observer')),
            ],
            options={
                'verbose_name_plural': 'Watchdogs',
                'verbose_name': 'Watchdog',
                'ordering': ('metric',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='watchdog',
            unique_together=set([('observer', 'metric')]),
        ),
    ]
