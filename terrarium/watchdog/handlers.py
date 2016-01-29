from django.conf import settings
from django.dispatch import receiver
from howl.models import Alert
from howl.signals import alert_clear, alert_notify, alert_wait

from terrarium.watchdog.pushover import PushoverApi


@receiver(alert_wait, sender=Alert)
def send_warning(sender, instance, compare_value, **kwargs):
    title = 'WARNING: {0}'.format(instance.observer.name)
    api = PushoverApi(settings.PUSHOVER_TOKEN)
    api.send_notification(
        settings.PUSHOVER_RECIPIENT, title, instance, compare_value, 'warning')


@receiver(alert_notify, sender=Alert)
def send_alert(sender, instance, compare_value, **kwargs):
    title = 'CRITICAL: {0}'.format(instance.observer.name)
    api = PushoverApi(settings.PUSHOVER_TOKEN)
    api.send_notification(
        settings.PUSHOVER_RECIPIENT, title, instance, compare_value, 'critical')


@receiver(alert_clear, sender=Alert)
def send_clear(sender, instance, compare_value, **kwargs):
    title = 'OK: {0}'.format(instance.observer.name)
    api = PushoverApi(settings.PUSHOVER_TOKEN)
    api.send_notification(
        settings.PUSHOVER_RECIPIENT, title, instance.observer, compare_value, 'ok')
