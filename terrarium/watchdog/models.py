from django.db import models
from howl.models import Observer

from didadata.models import Metric


class Watchdog(models.Model):
    observer = models.ForeignKey(Observer)
    metric = models.ForeignKey(Metric)

    class Meta:
        verbose_name = 'Watchdog'
        verbose_name_plural = 'Watchdogs'
        ordering = ('metric',)
        unique_together = ('observer', 'metric')

    def __str__(self):
        return '{0} - {1}'.format(self.observer, self.metric)

    @property
    def last_value(self):
        if not self.metric.record_set.first():
            return None

        return self.metric.record_set.first().value

    @property
    def last_time(self):
        if not self.metric.record_set.first():
            return None

        return self.metric.record_set.first().timestamp
