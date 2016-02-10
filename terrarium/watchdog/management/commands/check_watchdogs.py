import logging

from django.core.management.base import BaseCommand
from howl.models import Alert

from terrarium.watchdog.models import Watchdog


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.debug('>>  Checking watchdogs...')

        for watchdog in Watchdog.objects.all():
            if watchdog.max_age and watchdog.last_timestamp_delta > watchdog.max_age:
                Alert.set(
                    watchdog.last_timestamp,
                    identifier='watchdog:{0}'.format(watchdog.pk),
                    title='OUTDATED: {0}'.format(watchdog.metric)
                )
                continue
            else:
                Alert.clear(
                    watchdog.last_timestamp,
                    identifier='watchdog:{0}'.format(watchdog.pk),
                    title='OK: {0}'.format(watchdog.metric)
                )

            compare_value = watchdog.last_value
            watchdog.observer.compare(compare_value)

        logger.debug('>>  All watchdogs checked!')
