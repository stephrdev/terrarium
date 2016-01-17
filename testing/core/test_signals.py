import mock
import pytest
from howl.models import Alert

from didadata.tests.factories.metrics import MetricFactory, RecordFactory
from testing.factories.howl import ObserverFactory
from testing.factories.watchdog import WatchdogFactory


@pytest.mark.django_db
class TestSignals:

    def setup(self):
        self.metric = MetricFactory.create()
        self.observer = ObserverFactory.create(value=4)
        self.record = RecordFactory.create(value=5, metric=self.metric)
        self.watchdog = WatchdogFactory.create(observer=self.observer, metric=self.metric)

    @mock.patch('terrarium.core.signals.send_pushover_notification')
    def test_send_warning(self, pushover_mock):
        pushover_mock.return_value = None
        title = 'WARNING: {0}'.format(self.observer.name)

        assert self.watchdog.observer.compare(self.watchdog.last_measurement) is False
        Alert.objects.all().count() == 1
        alert = Alert.objects.first()
        assert pushover_mock.assert_called_once_with(title, alert, 'warning') is None

    @mock.patch('terrarium.core.signals.send_pushover_notification')
    def test_send_alert(self, pushover_mock):
        pushover_mock.return_value = None
        title_warning = 'WARNING: {0}'.format(self.observer.name)
        title_critical = 'CRITICAL: {0}'.format(self.observer.name)

        assert self.watchdog.observer.compare(self.watchdog.last_measurement) is False
        Alert.objects.all().count() == 1
        alert = Alert.objects.first()
        assert pushover_mock.assert_called_with(title_warning, alert, 'warning') is None
        assert self.watchdog.observer.compare(self.watchdog.last_measurement) is False
        Alert.objects.all().count() == 1
        assert pushover_mock.assert_called_with(title_critical, alert, 'critical') is None

    @mock.patch('terrarium.core.signals.send_pushover_notification')
    def test_send_clear(self, pushover_mock):
        pushover_mock.return_value = None
        title = 'OK: {0}'.format(self.observer.name)

        assert self.watchdog.observer.compare(self.watchdog.last_measurement) is False
        Alert.objects.all().count() == 1
        RecordFactory.create(value=4, metric=self.metric)
        assert self.watchdog.observer.compare(self.watchdog.last_measurement) is True
        assert pushover_mock.assert_called_with(title, self.watchdog.observer, 'ok') is None
        assert Alert.objects.all().count() == 0

    @mock.patch('terrarium.core.signals.logger')
    def test_pushover_notification_failed(self, mock_logger):
        assert self.watchdog.observer.compare(self.watchdog.last_measurement) is False
        assert mock_logger.critical.assert_called_with('application token is invalid') is None

    @mock.patch('requests.models.Response.ok')
    def test_pushover_notification(self, request_mock):
        request_mock.return_value = True

        assert self.watchdog.observer.compare(self.watchdog.last_measurement) is False
