import pytest
from django.utils.six import StringIO

from didadata.tests.factories.metrics import MetricFactory, RecordFactory
from terrarium.watchdog.management.commands.check_watchdogs import Command
from terrarium.watchdog.models import Watchdog
from testing.factories.watchdog import WatchdogFactory


@pytest.mark.django_db
class TestCommand:
    def setup(self):
        self.stdout = StringIO()

    def teardown(self):
        self.stdout.close()

    def test_handle(self, settings):
        settings.DEBUG = True
        metric = MetricFactory.create()
        RecordFactory.create(value=3, metric=metric)
        WatchdogFactory.create(metric=metric)

        assert Command().execute(stdout=self.stdout) is None

    def test_handle_compare_time(self, settings):
        settings.DEBUG = True
        metric = MetricFactory.create()
        RecordFactory.create(value=3, metric=metric)
        WatchdogFactory.create(metric=metric, compare_type=Watchdog.COMPARE_TIME)

        assert Command().execute(stdout=self.stdout) is None
