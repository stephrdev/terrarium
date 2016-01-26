import mock
import pytest
from requests import RequestException
from requests.models import Response

from didadata.tests.factories.metrics import MetricFactory, RecordFactory
from terrarium.watchdog.pushover import PushoverApi, PushoverException
from testing.factories.howl import ObserverFactory
from testing.factories.watchdog import WatchdogFactory


@pytest.mark.django_db
class TestPushoverApi:

    def setup(self):
        self.metric = MetricFactory.create()
        self.observer = ObserverFactory.create(value=4)
        self.record = RecordFactory.create(value=5, metric=self.metric)
        self.watchdog = WatchdogFactory.create(observer=self.observer, metric=self.metric)

    @mock.patch('requests.post')
    def test_send_message(self, request_mock):
        request_mock.return_value = Response()
        api = PushoverApi('SECRET_TOKEN')

        assert isinstance(api.send_message({}), Response) is True

    @mock.patch('requests.post')
    def test_send_message_exception(self, request_mock):
        request_mock.side_effect = RequestException
        api = PushoverApi('SECRET_TOKEN')

        with pytest.raises(PushoverException) as exc:
            api.send_message({})

        assert isinstance(exc.value.args[0], RequestException) is True

    @mock.patch('terrarium.watchdog.pushover.logger')
    def test_pushover_notification_failed(self, mock_logger):
        assert self.watchdog.observer.compare(self.watchdog.last_value) is False
        assert mock_logger.critical.assert_called_with('application token is invalid') is None

    @mock.patch('requests.models.Response.ok')
    def test_pushover_notification(self, request_mock):
        request_mock.return_value = True

        assert self.watchdog.observer.compare(self.watchdog.last_value) is False
