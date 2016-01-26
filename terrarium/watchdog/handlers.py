from django.conf import settings
from django.dispatch import receiver
from howl.models import Alert
from howl.signals import alert_clear, alert_notify, alert_wait

from terrarium.watchdog.pushover import PushoverApi


@receiver(alert_wait, sender=Alert)
def send_warning(sender, instance, **kwargs):
    title = 'WARNING: {0}'.format(instance.observer.name)
    api = PushoverApi(settings.PUSHOVER_TOKEN)
    api.send_notification(settings.PUSHOVER_RECIPIENT, title, instance, 'warning')


@receiver(alert_notify, sender=Alert)
def send_alert(sender, instance, **kwargs):
    title = 'CRITICAL: {0}'.format(instance.observer.name)
    api = PushoverApi(settings.PUSHOVER_TOKEN)
    api.send_notification(settings.PUSHOVER_RECIPIENT, title, instance, 'critical')


@receiver(alert_clear, sender=Alert)
def send_clear(sender, instance, **kwargs):
    title = 'OK: {0}'.format(instance.observer.name)
    api = PushoverApi(settings.PUSHOVER_TOKEN)
    api.send_notification(settings.PUSHOVER_RECIPIENT, title, instance.observer, 'ok')
