import mock
import pytest
import requests

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
        request_mock.return_value = requests.Response()
        api = PushoverApi('SECRET_TOKEN')

        assert isinstance(api.send_message({}), requests.Response) is True

    @mock.patch('requests.post')
    def test_send_message_exception(self, request_mock):
        request_mock.side_effect = requests.RequestException
        api = PushoverApi('SECRET_TOKEN')

        with pytest.raises(PushoverException) as exc:
            api.send_message({})

        assert isinstance(exc.value.args[0], requests.RequestException) is True

    @mock.patch('terrarium.watchdog.pushover.logger')
    @mock.patch('terrarium.watchdog.pushover.requests.post')
    def test_pushover_notification_failed(self, request_mock, mock_logger):
        request_mock.return_value = requests.Response()
        request_mock.return_value.status_code = 400
        request_mock.return_value._content = bytes(
            '{"errors": ["application token is invalid"]}', encoding='utf-8')

        with pytest.raises(PushoverException) as exc:
            assert self.watchdog.observer.compare(self.watchdog.last_value) is False

        assert exc.value.response == request_mock.return_value
        assert request_mock.called is True
        assert mock_logger.critical.assert_called_with('application token is invalid') is None

    @mock.patch('terrarium.watchdog.pushover.requests.post')
    def test_pushover_notification(self, request_mock):
        request_mock.return_value = requests.Response()
        request_mock.return_value.status_code = 200

        assert self.watchdog.observer.compare(self.watchdog.last_value) is False
        assert request_mock.called is True

    @mock.patch('terrarium.watchdog.pushover.logger')
    @mock.patch('terrarium.watchdog.pushover.requests.post')
    def test_pushover_unkown_error(self, request_mock, mock_logger):
        request_mock.return_value = requests.Response()
        request_mock.return_value.status_code = 400
        request_mock.return_value._content = bytes('foobar', encoding='utf-8')

        with pytest.raises(PushoverException) as exc:
            assert self.watchdog.observer.compare(self.watchdog.last_value) is False

        assert exc.value.response == request_mock.return_value
        assert request_mock.called is True
        assert mock_logger.critical.assert_called_with('Unkown error') is None
