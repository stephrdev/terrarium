from django.db import models
from django.utils import timezone
from howl.models import Observer

from didadata.models import Metric


class Watchdog(models.Model):
    observer = models.ForeignKey(Observer)
    metric = models.ForeignKey(Metric)
    max_age = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Watchdog'
        verbose_name_plural = 'Watchdogs'
        ordering = ('metric',)

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
        last_timestamp = self.last_timestamp
        if last_timestamp is None:
            return None

        td = timezone.now() - self.last_timestamp
        return td.total_seconds()
