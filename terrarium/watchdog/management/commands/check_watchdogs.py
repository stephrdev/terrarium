from django.core.management.base import BaseCommand

from ...utils import check_watchdogs


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_watchdogs()
