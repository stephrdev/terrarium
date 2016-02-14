import mock
import pytest
import requests
from django.utils.six import StringIO

from terrarium.watchdog.management.commands.check_watchdogs import Command
from testing.factories.didadata import MetricFactory, RecordFactory
from testing.factories.watchdog import WatchdogFactory


@pytest.mark.django_db
class TestCommand:

    def setup(self):
        self.stdout = StringIO()

    def teardown(self):
        self.stdout.close()

    @mock.patch('terrarium.watchdog.pushover.requests.post')
    def test_handle(self, request_mock, settings):
        request_mock.return_value = requests.Response()
        request_mock.return_value.status_code = 200

        settings.DEBUG = True
        metric = MetricFactory.create()
        RecordFactory.create(value=3, metric=metric)
        WatchdogFactory.create(metric=metric)

        assert Command().execute(stdout=self.stdout) is None
