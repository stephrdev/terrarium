import logging

import requests
from django.template.loader import render_to_string


logger = logging.getLogger(__name__)


class PushoverException(Exception):
    pass


class PushoverApi(object):

    def __init__(self, app_token):
        self.app_token = app_token

    def send_message(self, params):
        params.update({
            'token': self.app_token,
        })

        try:
            response = requests.post('https://api.pushover.net/1/messages.json', params=params)
            return response
        except requests.RequestException as e:
            raise PushoverException(e)

    def send_notification(self, recipient, title, obj, tpl):
        params = {
            'message': render_to_string('pushover/{0}.txt'.format(tpl), {'alert': obj}),
            'title': title,
            'user': recipient,
        }
        response = self.send_message(params)

        if not response.ok:
            logger.critical(', '.join(response.json()['errors']))
