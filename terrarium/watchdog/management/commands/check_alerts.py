import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import translation

from terrarium.watchdog.models import Watchdog


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        translation.activate(settings.LANGUAGE_CODE)

        logger.debug('>>  Checking alerts...')

        for data in Watchdog.objects.all():
            data.observer.compare(data.last_measurement)

        logger.debug('>>  All alerts checked!')
