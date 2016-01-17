import requests


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
