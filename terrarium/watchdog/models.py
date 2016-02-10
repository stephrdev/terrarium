from django.db import models
from django.utils import timezone
from howl.models import Observer

from didadata.models import Metric


class Watchdog(models.Model):
    COMPARE_VALUE, COMPARE_TIME = range(0, 2)
    COMPARE_CHOICES = (
        (COMPARE_VALUE, 'Compare value'),
        (COMPARE_TIME, 'Compare time'),
    )

    observer = models.ForeignKey(Observer)
    metric = models.ForeignKey(Metric)
    compare_type = models.PositiveIntegerField(
        'Compate type', choices=COMPARE_CHOICES, default=COMPARE_VALUE)

    class Meta:
        verbose_name = 'Watchdog'
        verbose_name_plural = 'Watchdogs'
        ordering = ('metric',)
        unique_together = ('observer', 'metric')

    def __str__(self):
        return '{0} - {1}'.format(self.observer, self.metric)

    @property
    def last_value(self):
        record = self.metric.record_set.first()
        return record.value if record is not None else None

    @property
    def last_timestamp(self):
        record = self.metric.record_set.first()
        return record.timestamp if record is not None else None

    @property
    def last_timestamp_delta(self):
        td = timezone.now() - self.last_timestamp
        return td.total_seconds()
