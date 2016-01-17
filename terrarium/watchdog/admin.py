from django.contrib import admin

from .models import Watchdog


@admin.register(Watchdog)
class WatchdogAdmin(admin.ModelAdmin):
    list_display = ('observer', 'metric', 'get_last_measurement', 'get_last_time')

    def get_last_measurement(self, obj):
        return obj.last_measurement

    get_last_measurement.short_description = 'Last measurement'

    def get_last_time(self, obj):
        return obj.last_time

    get_last_time.short_description = 'Last time'
