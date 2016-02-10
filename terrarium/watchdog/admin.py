from django.contrib import admin

from .models import Watchdog


@admin.register(Watchdog)
class WatchdogAdmin(admin.ModelAdmin):
    list_display = ('observer', 'metric', 'get_last_value', 'get_last_timestamp')

    def get_last_value(self, obj):
        return obj.last_value

    get_last_value.short_description = 'Last measurement'

    def get_last_timestamp(self, obj):
        return obj.last_timestamp

    get_last_timestamp.short_description = 'Last timestamp'
