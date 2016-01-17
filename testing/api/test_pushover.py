import mock
import pytest
from requests import RequestException
from requests.models import Response

from terrarium.api.pushover import PushoverApi, PushoverException


class TestPushoverApi:

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
