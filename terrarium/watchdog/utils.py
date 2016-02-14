from howl.models import Alert

from .models import Watchdog


def check_watchdogs():
    all_clear = True
    for watchdog in Watchdog.objects.all():
        if watchdog.max_age and watchdog.last_timestamp_delta > watchdog.max_age:
            Alert.set(
                watchdog.last_timestamp,
                identifier='watchdog:{0}'.format(watchdog.pk),
                title='OUTDATED: {0}'.format(watchdog.metric)
            )
            all_clear = False
            continue
        else:
            Alert.clear(
                watchdog.last_timestamp,
                identifier='watchdog:{0}'.format(watchdog.pk),
                title='OK: {0}'.format(watchdog.metric)
            )

        compare_value = watchdog.last_value
        if not watchdog.observer.compare(compare_value):
            all_clear = False

    return all_clear
