from django.apps import AppConfig


class WatchdogConfig(AppConfig):
    name = 'terrarium.watchdog'

    def ready(self):
        import terrarium.watchdog.signals  # NOQA
