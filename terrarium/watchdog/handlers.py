import logging

from django.conf import settings
from django.dispatch import receiver
from django.template.loader import render_to_string
from howl.models import Alert
from howl.signals import alert_clear, alert_notify, alert_wait

from terrarium.watchdog.pushover import PushoverApi


logger = logging.getLogger(__name__)


def send_pushover_notification(title, obj, tpl):
    api = PushoverApi(settings.PUSHOVER_TOKEN)
    params = {
        'message': render_to_string('pushover/{0}.txt'.format(tpl), {'alert': obj}),
        'title': title,
        'user': settings.PUSHOVER_RECIPIENT,
    }
    response = api.send_message(params)

    if not response.ok:
        logger.critical(', '.join(response.json()['errors']))


@receiver(alert_wait, sender=Alert)
def send_warning(sender, instance, **kwargs):
    title = 'WARNING: {0}'.format(instance.observer.name)
    send_pushover_notification(title, instance, 'warning')


@receiver(alert_notify, sender=Alert)
def send_alert(sender, instance, **kwargs):
    title = 'CRITICAL: {0}'.format(instance.observer.name)
    send_pushover_notification(title, instance, 'critical')


@receiver(alert_clear, sender=Alert)
def send_clear(sender, instance, **kwargs):
    title = 'OK: {0}'.format(instance.observer.name)
    send_pushover_notification(title, instance.observer, 'ok')
