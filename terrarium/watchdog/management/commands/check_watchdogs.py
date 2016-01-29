import logging

from django.core.management.base import BaseCommand

from terrarium.watchdog.models import Watchdog


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.debug('>>  Checking watchdogs...')

        for watchdog in Watchdog.objects.all():
            watchdog.observer.compare(watchdog.last_value)

        logger.debug('>>  All watchdogs checked!')
