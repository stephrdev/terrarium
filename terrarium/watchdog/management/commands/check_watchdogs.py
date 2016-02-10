import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from terrarium.watchdog.models import Watchdog
from terrarium.watchdog.pushover import PushoverApi


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.debug('>>  Checking watchdogs...')

        for watchdog in Watchdog.objects.all():
            if watchdog.max_age and watchdog.last_timestamp_delta > watchdog.max_age:
                title = 'OUTDATED: {0}'.format(watchdog.metric)
                api = PushoverApi(settings.PUSHOVER_TOKEN)
                api.send_notification(
                    settings.PUSHOVER_RECIPIENT, title, 'outdated',
                    last_timestamp=watchdog.last_timestamp
                )
                continue

            compare_value = watchdog.last_value
            watchdog.observer.compare(compare_value)

        logger.debug('>>  All watchdogs checked!')
