import mock
import pytest
from howl.models import Alert

from testing.factories.didadata import MetricFactory, RecordFactory
from testing.factories.howl import ObserverFactory
from testing.factories.watchdog import WatchdogFactory


@pytest.mark.django_db
class TestSignals:

    def setup(self):
        self.metric = MetricFactory.create()
        self.observer = ObserverFactory.create(value=4)
        self.record = RecordFactory.create(value=5, metric=self.metric)
        self.watchdog = WatchdogFactory.create(observer=self.observer, metric=self.metric)

    @mock.patch('terrarium.watchdog.pushover.PushoverApi.send_notification')
    def test_send_warning(self, pushover_mock, settings):
        pushover_mock.return_value = None
        title = 'WARNING: {0}'.format(self.observer.name)

        assert self.watchdog.observer.compare(self.watchdog.last_value) is False
        Alert.objects.all().count() == 1
        alert = Alert.objects.first()
        pushover_mock.assert_called_once_with(
            settings.PUSHOVER_RECIPIENT, title, 'warning', alert=alert,
            observer=self.watchdog.observer, value=self.watchdog.last_value
        )

    @mock.patch('terrarium.watchdog.pushover.PushoverApi.send_notification')
    def test_send_alert(self, pushover_mock, settings):
        pushover_mock.return_value = None
        self.observer.waiting_period = 0
        title_critical = 'CRITICAL: {0}'.format(self.observer.name)

        assert self.watchdog.observer.compare(self.watchdog.last_value) is False
        alert = Alert.objects.first()
        Alert.objects.all().count() == 1
        pushover_mock.assert_called_with(
            settings.PUSHOVER_RECIPIENT, title_critical, 'critical', alert=alert,
            observer=self.watchdog.observer, value=self.watchdog.last_value,
        )

    @mock.patch('terrarium.watchdog.pushover.PushoverApi.send_notification')
    def test_send_clear(self, pushover_mock, settings):
        pushover_mock.return_value = None
        title = 'OK: {0}'.format(self.observer.name)

        assert self.watchdog.observer.compare(self.watchdog.last_value) is False
        Alert.objects.all().count() == 1
        RecordFactory.create(value=4, metric=self.metric)
        assert self.watchdog.observer.compare(self.watchdog.last_value) is True
        assert pushover_mock.call_args[0] == (settings.PUSHOVER_RECIPIENT, title, 'ok')
        assert Alert.objects.all().count() == 0
