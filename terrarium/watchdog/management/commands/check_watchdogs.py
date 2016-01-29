import logging

from django.core.management.base import BaseCommand

from terrarium.watchdog.models import Watchdog


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.debug('>>  Checking watchdogs...')

        for watchdog in Watchdog.objects.all():
            compare_value = watchdog.last_value
            if watchdog.compare_type == Watchdog.COMPARE_TIME:
                compare_value = watchdog.last_time_delta

            watchdog.observer.compare(compare_value)

        logger.debug('>>  All watchdogs checked!')
